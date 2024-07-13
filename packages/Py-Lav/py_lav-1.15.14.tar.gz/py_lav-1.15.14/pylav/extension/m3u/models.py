from __future__ import annotations

import decimal
import errno
import os
from typing import Any

import aiopath

from pylav.extension.m3u.mixins import BasePathMixin, GroupedBasePathMixin
from pylav.extension.m3u.parser import format_date_time, parse
from pylav.extension.m3u.protocols import EXT_X_KEY, EXT_X_MAP, EXT_X_SESSION_KEY, EXT_X_START


class MalformedPlaylistError(Exception):
    pass


class M3U8:
    __slots__ = (
        "data",
        "_base_uri",
        "keys",
        "segments",
        "files",
        "media",
        "playlists",
        "iframe_playlists",
        "segment_map",
        "start",
        "server_control",
        "part_inf",
        "skip",
        "rendition_reports",
        "session_data",
        "session_keys",
        "preload_hint",
        "content_steering",
        "_base_path",
        "is_variant",
        "is_independent_segments",
        "media_sequence",
        "discontinuity_sequence",
        "allow_cache",
        "version",
        "target_duration",
        "playlist_type",
        "is_i_frames_only",
        "is_endlist",
    )

    simple_attributes = (
        # obj attribute      # parser attribute
        ("is_variant", "is_variant"),
        ("is_endlist", "is_endlist"),
        ("is_i_frames_only", "is_i_frames_only"),
        ("target_duration", "targetduration"),
        ("media_sequence", "media_sequence"),
        ("program_date_time", "program_date_time"),
        ("is_independent_segments", "is_independent_segments"),
        ("version", "version"),
        ("allow_cache", "allow_cache"),
        ("playlist_type", "playlist_type"),
        ("discontinuity_sequence", "discontinuity_sequence"),
    )

    def __init__(
        self,
        content: str = None,
        base_path: str = None,
        base_uri: str = None,
        strict: bool = False,
        custom_tags_parser=None,
    ) -> None:
        self.is_variant = False

        if content is not None:
            self.data = parse(content, strict, custom_tags_parser)
        else:
            self.data = {}
        self._base_uri = base_uri
        if self._base_uri and not self._base_uri.endswith("/"):
            self._base_uri += "/"

        self._initialize_attributes()
        self.base_path = base_path

    def _initialize_attributes(self) -> None:
        self.keys = [Key(base_uri=self.base_uri, **params) if params else None for params in self.data.get("keys", [])]
        self.segments = SegmentList(
            [
                Segment(base_uri=self.base_uri, keyobject=find_key(segment.get("key", {}), self.keys), **segment)
                for segment in self.data.get("segments", [])
            ]
        )
        # self.keys = get_uniques([ segment.key for segment in self.segments ])
        for attr, param in self.simple_attributes:
            setattr(self, attr, self.data.get(param))

        self.files = [key.uri for key in self.keys if key and key.uri not in self.files]

        self.files.extend(self.segments.uri)

        self.media = MediaList([Media(base_uri=self.base_uri, **media) for media in self.data.get("media", [])])

        self.playlists = PlaylistList(
            [
                Playlist(base_uri=self.base_uri, media=self.media, **playlist)
                for playlist in self.data.get("playlists", [])
            ]
        )

        self.iframe_playlists = PlaylistList()
        for ifr_pl in self.data.get("iframe_playlists", []):
            self.iframe_playlists.append(
                IFramePlaylist(
                    base_uri=self.base_uri, uri=ifr_pl["uri"], iframe_stream_info=ifr_pl["iframe_stream_info"]
                )
            )
        self.segment_map = self.data.get("segment_map")

        start = self.data.get("start", None)
        self.start = start and Start(**start)

        server_control = self.data.get("server_control", None)
        self.server_control = server_control and ServerControl(**server_control)

        part_inf = self.data.get("part_inf", None)
        self.part_inf = part_inf and PartInformation(**part_inf)

        skip = self.data.get("skip", None)
        self.skip = skip and Skip(**skip)

        self.rendition_reports = RenditionReportList(
            [
                RenditionReport(base_uri=self.base_uri, **rendition_report)
                for rendition_report in self.data.get("rendition_reports", [])
            ]
        )

        self.session_data = SessionDataList(
            [
                SessionData(**session_data)
                for session_data in self.data.get("session_data", [])
                if "data_id" in session_data
            ]
        )

        self.session_keys = [
            SessionKey(base_uri=self.base_uri, **params) if params else None
            for params in self.data.get("session_keys", [])
        ]

        preload_hint = self.data.get("preload_hint", None)
        self.preload_hint = preload_hint and PreloadHint(base_uri=self.base_uri, **preload_hint)

        content_steering = self.data.get("content_steering", None)
        self.content_steering = content_steering and ContentSteering(base_uri=self.base_uri, **content_steering)

    def __unicode__(self) -> str:
        return self.dumps()

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, new_base_uri: str | None) -> None:
        self._base_uri = new_base_uri
        self.media.base_uri = new_base_uri
        self.playlists.base_uri = new_base_uri
        self.iframe_playlists.base_uri = new_base_uri
        self.segments.base_uri = new_base_uri
        self.rendition_reports.base_uri = new_base_uri
        for key in self.keys:
            if key:
                key.base_uri = new_base_uri
        for key in self.session_keys:
            if key:
                key.base_uri = new_base_uri
        if self.preload_hint:
            self.preload_hint.base_uri = new_base_uri
        if self.content_steering:
            self.content_steering.base_uri = new_base_uri

    @property
    def base_path(self) -> str:
        return self._base_path

    @base_path.setter
    def base_path(self, newbase_path: str):
        self._base_path = newbase_path
        self._update_base_path()

    def _update_base_path(self) -> None:
        if self._base_path is None:
            return
        for key in self.keys:
            if key:
                key.base_path = self._base_path
        for key in self.session_keys:
            if key:
                key.base_path = self._base_path
        self.media.base_path = self._base_path
        self.segments.base_path = self._base_path
        self.playlists.base_path = self._base_path
        self.iframe_playlists.base_path = self._base_path
        self.rendition_reports.base_path = self._base_path
        if self.preload_hint:
            self.preload_hint.base_path = self._base_path
        if self.content_steering:
            self.content_steering.base_path = self._base_path

    def add_playlist(self, playlist: Playlist) -> None:
        self.is_variant = True
        self.playlists.append(playlist)

    def add_iframe_playlist(self, iframe_playlist: IFramePlaylist | None) -> None:
        if iframe_playlist is not None:
            self.is_variant = True
            self.iframe_playlists.append(iframe_playlist)

    def add_media(self, media: Media) -> None:
        self.media.append(media)

    def add_segment(self, segment: Segment) -> None:
        self.segments.append(segment)

    def add_rendition_report(self, report: RenditionReport) -> None:
        self.rendition_reports.append(report)

    def dumps(self) -> str:
        """
        Returns the current m3u8 as a string.
        You could also use unicode(<this obj>) or str(<this obj>)
        """
        output = ["#EXTM3U"]

        if self.content_steering:
            output.append(str(self.content_steering))
        if self.is_independent_segments:
            output.append("#EXT-X-INDEPENDENT-SEGMENTS")
        if self.media_sequence:
            output.append(f"#EXT-X-MEDIA-SEQUENCE:{str(self.media_sequence)}")
        if self.discontinuity_sequence:
            output.append(f"#EXT-X-DISCONTINUITY-SEQUENCE:{number_to_string(self.discontinuity_sequence)}")
        if self.allow_cache:
            output.append(f"#EXT-X-ALLOW-CACHE:{self.allow_cache.upper()}")
        if self.version:
            output.append(f"#EXT-X-VERSION:{str(self.version)}")
        if self.target_duration:
            output.append(f"#EXT-X-TARGETDURATION:{number_to_string(self.target_duration)}")
        if self.playlist_type is not None and self.playlist_type != "":
            output.append(f"#EXT-X-PLAYLIST-TYPE:{str(self.playlist_type).upper()}")

        if self.start:
            output.append(str(self.start))
        if self.is_i_frames_only:
            output.append("#EXT-X-I-FRAMES-ONLY")
        if self.server_control:
            output.append(str(self.server_control))
        if self.is_variant:
            if self.media:
                output.append(str(self.media))
            output.append(str(self.playlists))
            if self.iframe_playlists:
                output.append(str(self.iframe_playlists))
        if self.part_inf:
            output.append(str(self.part_inf))
        if self.skip:
            output.append(str(self.skip))
        if self.session_data:
            output.append(str(self.session_data))

        output.extend(str(key) for key in self.session_keys)
        output.append(str(self.segments))

        if self.preload_hint:
            output.append(str(self.preload_hint))

        if self.rendition_reports:
            output.append(str(self.rendition_reports))

        if self.is_endlist:
            output.append("#EXT-X-ENDLIST")

        # ensure that the last line is terminated correctly
        if output[-1] and not output[-1].endswith("\n"):
            output.append("")

        return "\n".join(output)

    async def dump(self, filename: str) -> None:
        """
        Saves the current m3u8 to ``filename``
        """
        self._create_sub_directories(filename)
        file = aiopath.AsyncPath(filename)
        async with file.open("w") as fileobj:
            await fileobj.write(self.dumps())

    @staticmethod
    def _create_sub_directories(filename: str) -> None:
        basename = os.path.dirname(filename)
        try:
            if basename:
                os.makedirs(basename)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise


class Segment(BasePathMixin):
    """
    A video segment from a M3U8 playlist

    `uri`
      a string with the segment uri

    `title`
      title attribute from EXTINF parameter

    `program_date_time`
      Returns the EXT-X-PROGRAM-DATE-TIME as a datetime. This field is only set
      if EXT-X-PROGRAM-DATE-TIME exists for this segment
      http://tools.ietf.org/html/draft-pantos-http-live-streaming-07#section-3.3.5

    `current_program_date_time`
      Returns a datetime of this segment, either the value of `program_date_time`
      when EXT-X-PROGRAM-DATE-TIME is set or a calculated value based on previous
      segments' EXT-X-PROGRAM-DATE-TIME and EXTINF values

    `discontinuity`
      Returns a boolean indicating if a EXT-X-DISCONTINUITY tag exists
      http://tools.ietf.org/html/draft-pantos-http-live-streaming-13#section-3.4.11

    `cue_out_start`
      Returns a boolean indicating if a EXT-X-CUE-OUT tag exists

    `cue_out`
      Returns a boolean indicating if a EXT-X-CUE-OUT-CONT tag exists
      Note: for backwards compatibility, this will be True when cue_out_start
            is True, even though this tag did not exist in the input, and
            EXT-X-CUE-OUT-CONT will not exist in the output

    `cue_in`
      Returns a boolean indicating if a EXT-X-CUE-IN tag exists

    `scte35`
      Base64 encoded SCTE35 metadata if available

    `scte35_duration`
      Planned SCTE35 duration

    `duration`
      duration attribute from EXTINF parameter

    `base_uri`
      uri the key comes from in URI hierarchy. ex.: http://example.com/path/to

    `bitrate`
      bitrate attribute from EXT-X-BITRATE parameter

    `byterange`
      byterange attribute from EXT-X-BYTERANGE parameter

    `key`
      Key used to encrypt the segment (EXT-X-KEY)

    `parts`
      partial segments that make up this segment

    `dateranges`
      any dateranges that should precede the segment

    `gap_tag`
      GAP tag indicates that a Media Segment is missing

    `custom_parser_values`
        Additional values which custom_tags_parser might store per segment
    """

    def __init__(
        self,
        uri=None,
        base_uri=None,
        program_date_time=None,
        current_program_date_time=None,
        duration=None,
        title=None,
        bitrate=None,
        byterange=None,
        cue_out=False,
        cue_out_start=False,
        cue_in=False,
        discontinuity=False,
        key=None,  # noqa
        scte35=None,
        scte35_duration=None,
        keyobject=None,
        parts=None,
        init_section=None,
        dateranges=None,
        gap_tag=None,
        custom_parser_values=None,
    ):
        self.uri = uri
        self.duration = duration
        self.title = title
        self._base_uri = base_uri
        self.bitrate = bitrate
        self.byterange = byterange
        self.program_date_time = program_date_time
        self.current_program_date_time = current_program_date_time
        self.discontinuity = discontinuity
        self.cue_out_start = cue_out_start
        self.cue_out = cue_out
        self.cue_in = cue_in
        self.scte35 = scte35
        self.scte35_duration = scte35_duration
        self.key = keyobject
        self.parts = PartialSegmentList(
            [PartialSegment(base_uri=self._base_uri, **partial) for partial in parts] if parts else []
        )
        if init_section is not None:
            self.init_section = InitializationSection(self._base_uri, **init_section)
        else:
            self.init_section = None
        self.dateranges = DateRangeList([DateRange(**daterange) for daterange in dateranges] if dateranges else [])
        self.gap_tag = gap_tag
        self.custom_parser_values = custom_parser_values or {}

        # Key(base_uri=base_uri, **key) if key else None

    def add_part(self, part: PartInformation) -> None:
        self.parts.append(part)

    def dumps(self, last_segment: Segment | None) -> str:
        output = []

        if (
            (not last_segment or self.key == last_segment.key)
            and self.key
            and last_segment is None
            or last_segment
            and self.key != last_segment.key
        ):
            output.extend((str(self.key), "\n"))
        if last_segment and self.init_section != last_segment.init_section and not self.init_section:
            raise MalformedPlaylistError("init section can't be None if previous is not None")
        elif (
            last_segment
            and self.init_section != last_segment.init_section
            or self.init_section
            and last_segment is None
        ):
            output.extend((str(self.init_section), "\n"))
        if self.discontinuity:
            output.append("#EXT-X-DISCONTINUITY\n")
        if self.program_date_time:
            output.append(f"#EXT-X-PROGRAM-DATE-TIME:{format_date_time(self.program_date_time)}\n")

        if len(self.dateranges):
            output.extend((str(self.dateranges), "\n"))
        if self.cue_out_start:
            output.append(f"#EXT-X-CUE-OUT{f':{self.scte35_duration}' if self.scte35_duration else ''}\n")

        elif self.cue_out:
            output.append("#EXT-X-CUE-OUT-CONT\n")
        if self.cue_in:
            output.append("#EXT-X-CUE-IN\n")

        if self.parts:
            output.extend((str(self.parts), "\n"))
        if self.uri:
            if self.duration is not None:
                output.append(f"#EXTINF:{number_to_string(self.duration)},")
                if self.title:
                    output.append(self.title)
                output.append("\n")

            if self.byterange:
                output.append(f"#EXT-X-BYTERANGE:{self.byterange}\n")

            if self.bitrate:
                output.append(f"#EXT-X-BITRATE:{self.bitrate}\n")

            if self.gap_tag:
                output.append("#EXT-X-GAP\n")

            output.append(self.uri)

        return "".join(output)

    def __str__(self) -> str:
        return self.dumps(None)

    @property
    def base_path(self) -> str | None:
        return super().base_path

    @base_path.setter
    def base_path(self, newbase_path: str | None) -> None:
        super(Segment, self.__class__).base_path.fset(self, newbase_path)  # type: ignore
        self.parts.base_path = newbase_path
        if self.init_section is not None:
            self.init_section.base_path = newbase_path

    @property
    def base_uri(self) -> str | None:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, newbase_uri: str | None) -> None:
        self._base_uri = newbase_uri
        self.parts.base_uri = newbase_uri
        if self.init_section is not None:
            self.init_section.base_uri = newbase_uri


class SegmentList(list, GroupedBasePathMixin):
    def __str__(self) -> str:
        output = []
        last_segment = None
        for segment in self:
            output.append(segment.dumps(last_segment))
            last_segment = segment
        return "\n".join(output)

    @property
    def uri(self) -> list[str]:
        return [seg.uri for seg in self]

    def by_key(self, key: Key) -> list[Segment]:
        return [segment for segment in self if segment.key == key]


class PartialSegment(BasePathMixin):
    __slots__ = (
        "uri",
        "base_uri",
        "duration",
        "program_date_time",
        "current_program_date_time",
        "byterange",
        "independent",
        "gap",
        "dateranges",
        "gap_tag",
    )

    def __init__(
        self,
        base_uri,
        uri,
        duration,
        program_date_time=None,
        current_program_date_time=None,
        byterange=None,
        independent=None,
        gap=None,
        dateranges=None,
        gap_tag=None,
    ) -> None:
        self.base_uri = base_uri
        self.uri = uri
        self.duration = duration
        self.program_date_time = program_date_time
        self.current_program_date_time = current_program_date_time
        self.byterange = byterange
        self.independent = independent
        self.gap = gap
        self.dateranges = DateRangeList([DateRange(**daterange) for daterange in dateranges] if dateranges else [])
        self.gap_tag = gap_tag

    def dumps(self, last_segment: Segment | None) -> str:  # noqa
        output = []

        if len(self.dateranges):
            output.extend((str(self.dateranges), "\n"))
        if self.gap_tag:
            output.append("#EXT-X-GAP\n")

        output.append(f'#EXT-X-PART:DURATION={number_to_string(self.duration)},URI="{self.uri}"')

        if self.independent:
            output.append(f",INDEPENDENT={self.independent}")

        if self.byterange:
            output.append(f",BYTERANGE={self.byterange}")

        if self.gap:
            output.append(f",GAP={self.gap}")

        return "".join(output)

    def __str__(self) -> str:
        return self.dumps(None)


class PartialSegmentList(list, GroupedBasePathMixin):
    def __str__(self) -> str:
        output = [str(part) for part in self]
        return "\n".join(output)


class Key(BasePathMixin):
    tag = EXT_X_KEY

    def __init__(self, method, base_uri, uri=None, iv=None, keyformat=None, keyformatversions=None, **kwargs):
        self.method = method
        self.uri = uri
        self.iv = iv
        self.keyformat = keyformat
        self.keyformatversions = keyformatversions
        self.base_uri = base_uri
        self._extra_params = kwargs

    def __str__(self) -> str:
        output = [
            f"METHOD={self.method}",
        ]
        if self.uri:
            output.append(f'URI="{self.uri}"')
        if self.iv:
            output.append(f"IV={self.iv}")
        if self.keyformat:
            output.append(f'KEYFORMAT="{self.keyformat}"')
        if self.keyformatversions:
            output.append(f'KEYFORMATVERSIONS="{self.keyformatversions}"')

        return f"{self.tag}:{','.join(output)}"

    def __eq__(self, other: Key) -> bool:
        return (
            (
                self.method == other.method
                and self.uri == other.uri
                and self.iv == other.iv
                and self.base_uri == other.base_uri
                and self.keyformat == other.keyformat
                and self.keyformatversions == other.keyformatversions
            )
            if other
            else False
        )

    def __ne__(self, other: Key) -> bool:
        return not self.__eq__(other)


class InitializationSection(BasePathMixin):
    tag = EXT_X_MAP

    def __init__(self, base_uri, uri, byterange=None) -> None:
        self.base_uri = base_uri
        self.uri = uri
        self.byterange = byterange

    def __str__(self) -> str:
        output = []
        if self.uri:
            output.append(f"URI={quoted(self.uri)}")
        if self.byterange:
            output.append(f"BYTERANGE={self.byterange}")
        return f"{self.tag}:{','.join(output)}"

    def __eq__(self, other: InitializationSection) -> bool:
        return (
            self.uri == other.uri and self.byterange == other.byterange and self.base_uri == other.base_uri
            if other
            else False
        )

    def __ne__(self, other: InitializationSection) -> bool:
        return not self.__eq__(other)


class SessionKey(Key):
    tag = EXT_X_SESSION_KEY


class Playlist(BasePathMixin):
    def __init__(self, uri, stream_info, media, base_uri) -> None:
        self.uri = uri
        self.base_uri = base_uri

        if (resolution := stream_info.get("resolution")) is not None:
            resolution = resolution.strip('"')
            values = resolution.split("x")
            resolution_pair = (int(values[0]), int(values[1]))
        else:
            resolution_pair = None

        self.stream_info = StreamInfo(
            bandwidth=stream_info["bandwidth"],
            video=stream_info.get("video"),
            audio=stream_info.get("audio"),
            subtitles=stream_info.get("subtitles"),
            closed_captions=stream_info.get("closed_captions"),
            average_bandwidth=stream_info.get("average_bandwidth"),
            program_id=stream_info.get("program_id"),
            resolution=resolution_pair,
            codecs=stream_info.get("codecs"),
            frame_rate=stream_info.get("frame_rate"),
            video_range=stream_info.get("video_range"),
            hdcp_level=stream_info.get("hdcp_level"),
            pathway_id=stream_info.get("pathway_id"),
        )
        self.media = []
        for media_type in ("audio", "video", "subtitles"):
            if group_id := stream_info.get(media_type):
                self.media += filter(lambda m: m.group_id == group_id, media)

    def __str__(self) -> str:
        media_types = []
        stream_inf = [str(self.stream_info)]
        for media in self.media:
            if media.type in media_types:
                continue
            media_types += [media.type]
            media_type = media.type.upper()
            stream_inf.append(f'{media_type}="{media.group_id}"')

        return f"#EXT-X-STREAM-INF:{','.join(stream_inf)}\n{self.uri}"


class IFramePlaylist(BasePathMixin):
    def __init__(self, base_uri, uri, iframe_stream_info) -> None:
        self.uri = uri
        self.base_uri = base_uri

        if (resolution := iframe_stream_info.get("resolution")) is not None:
            values = resolution.split("x")
            resolution_pair = (int(values[0]), int(values[1]))
        else:
            resolution_pair = None

        self.iframe_stream_info = StreamInfo(
            bandwidth=iframe_stream_info.get("bandwidth"),
            average_bandwidth=iframe_stream_info.get("average_bandwidth"),
            video=iframe_stream_info.get("video"),
            # Audio, subtitles, and closed captions should not exist in
            # EXT-X-I-FRAME-STREAM-INF, so just hardcode them to None.
            audio=None,
            subtitles=None,
            closed_captions=None,
            program_id=iframe_stream_info.get("program_id"),
            resolution=resolution_pair,
            codecs=iframe_stream_info.get("codecs"),
            video_range=iframe_stream_info.get("video_range"),
            hdcp_level=iframe_stream_info.get("hdcp_level"),
            frame_rate=None,
            pathway_id=iframe_stream_info.get("pathway_id"),
        )

    def __str__(self) -> str:
        iframe_stream_inf = []
        if self.iframe_stream_info.program_id:
            iframe_stream_inf.append(f"PROGRAM-ID={self.iframe_stream_info.program_id:d}")
        if self.iframe_stream_info.bandwidth:
            iframe_stream_inf.append(f"BANDWIDTH={self.iframe_stream_info.bandwidth:d}")
        if self.iframe_stream_info.average_bandwidth:
            iframe_stream_inf.append(f"AVERAGE-BANDWIDTH={self.iframe_stream_info.average_bandwidth:d}")
        if self.iframe_stream_info.resolution:
            res = f"{self.iframe_stream_info.resolution[0]}x{self.iframe_stream_info.resolution[1]}"
            iframe_stream_inf.append(f"RESOLUTION={res}")
        if self.iframe_stream_info.codecs:
            iframe_stream_inf.append(f"CODECS={quoted(self.iframe_stream_info.codecs)}")
        if self.iframe_stream_info.video_range:
            iframe_stream_inf.append(f"VIDEO-RANGE={self.iframe_stream_info.video_range}")
        if self.iframe_stream_info.hdcp_level:
            iframe_stream_inf.append(f"HDCP-LEVEL={self.iframe_stream_info.hdcp_level}")
        if self.uri:
            iframe_stream_inf.append(f"URI={quoted(self.uri)}")
        if self.iframe_stream_info.pathway_id:
            iframe_stream_inf.append(f"PATHWAY-ID={quoted(self.iframe_stream_info.pathway_id)}")

        return f"#EXT-X-I-FRAME-STREAM-INF:{','.join(iframe_stream_inf)}"


class StreamInfo:
    bandwidth = None
    closed_captions = None
    average_bandwidth = None
    program_id = None
    resolution = None
    codecs = None
    audio = None
    video = None
    subtitles = None
    frame_rate = None
    video_range = None
    hdcp_level = None
    pathway_id = None

    def __init__(self, **kwargs: Any) -> None:
        self.bandwidth = kwargs.get("bandwidth")
        self.closed_captions = kwargs.get("closed_captions")
        self.average_bandwidth = kwargs.get("average_bandwidth")
        self.program_id = kwargs.get("program_id")
        self.resolution = kwargs.get("resolution")
        self.codecs = kwargs.get("codecs")
        self.audio = kwargs.get("audio")
        self.video = kwargs.get("video")
        self.subtitles = kwargs.get("subtitles")
        self.frame_rate = kwargs.get("frame_rate")
        self.video_range = kwargs.get("video_range")
        self.hdcp_level = kwargs.get("hdcp_level")
        self.pathway_id = kwargs.get("pathway_id")

    def __str__(self) -> str:
        stream_inf = []
        if self.program_id is not None:
            stream_inf.append(f"PROGRAM-ID={self.program_id:d}")
        if self.closed_captions is not None:
            stream_inf.append(f"CLOSED-CAPTIONS={self.closed_captions}")
        if self.bandwidth is not None:
            stream_inf.append(f"BANDWIDTH={self.bandwidth:d}")
        if self.average_bandwidth is not None:
            stream_inf.append(f"AVERAGE-BANDWIDTH={self.average_bandwidth:d}")
        if self.resolution is not None:
            res = f"{self.resolution[0]}x{self.resolution[1]}"
            stream_inf.append(f"RESOLUTION={res}")
        if self.frame_rate is not None:
            stream_inf.append(f"FRAME-RATE={decimal.Decimal(self.frame_rate).quantize(decimal.Decimal('1.000')):g}")
        if self.codecs is not None:
            stream_inf.append(f"CODECS={quoted(self.codecs)}")
        if self.video_range is not None:
            stream_inf.append(f"VIDEO-RANGE={self.video_range}")
        if self.hdcp_level is not None:
            stream_inf.append(f"HDCP-LEVEL={self.hdcp_level}")
        if self.pathway_id is not None:
            stream_inf.append(f"PATHWAY-ID={quoted(self.pathway_id)}")
        return ",".join(stream_inf)


class Media(BasePathMixin):
    def __init__(
        self,
        uri=None,
        type=None,  # noqa
        group_id=None,
        language=None,
        name=None,
        default=None,
        autoselect=None,
        forced=None,
        characteristics=None,
        channels=None,
        assoc_language=None,
        instream_id=None,
        base_uri=None,
        **extras,
    ) -> None:
        self.base_uri = base_uri
        self.uri = uri
        self.type = type
        self.group_id = group_id
        self.language = language
        self.name = name
        self.default = default
        self.autoselect = autoselect
        self.forced = forced
        self.assoc_language = assoc_language
        self.instream_id = instream_id
        self.characteristics = characteristics
        self.channels = channels
        self.extras = extras

    def dumps(self) -> str:
        media_out = []

        if self.uri:
            media_out.append(f"URI={quoted(self.uri)}")
        if self.type:
            media_out.append(f"TYPE={self.type}")
        if self.group_id:
            media_out.append(f"GROUP-ID={quoted(self.group_id)}")
        if self.language:
            media_out.append(f"LANGUAGE={quoted(self.language)}")
        if self.assoc_language:
            media_out.append(f"ASSOC-LANGUAGE={quoted(self.assoc_language)}")
        if self.name:
            media_out.append(f"NAME={quoted(self.name)}")
        if self.default:
            media_out.append(f"DEFAULT={self.default}")
        if self.autoselect:
            media_out.append(f"AUTOSELECT={self.autoselect}")
        if self.forced:
            media_out.append(f"FORCED={self.forced}")
        if self.instream_id:
            media_out.append(f"INSTREAM-ID={quoted(self.instream_id)}")
        if self.characteristics:
            media_out.append(f"CHARACTERISTICS={quoted(self.characteristics)}")
        if self.channels:
            media_out.append(f"CHANNELS={quoted(self.channels)}")

        return f'#EXT-X-MEDIA:{",".join(media_out)}'

    def __str__(self) -> str:
        return self.dumps()


class TagList(list):
    def __str__(self) -> str:
        output = [str(tag) for tag in self]
        return "\n".join(output)


class MediaList(TagList, GroupedBasePathMixin):
    @property
    def uri(self) -> list[str]:
        return [media.uri for media in self]


class PlaylistList(TagList, GroupedBasePathMixin):
    pass


class SessionDataList(TagList):
    pass


class Start:
    def __init__(self, time_offset, precise=None) -> None:
        self.time_offset = float(time_offset)
        self.precise = precise

    def __str__(self) -> str:
        output = [f"TIME-OFFSET={str(self.time_offset)}"]
        if self.precise and self.precise in ["YES", "NO"]:
            output.append(f"PRECISE={str(self.precise)}")

        return f"{EXT_X_START}:{','.join(output)}"


class RenditionReport(BasePathMixin):
    def __init__(self, base_uri, uri, last_msn, last_part=None) -> None:
        self.base_uri = base_uri
        self.uri = uri
        self.last_msn = last_msn
        self.last_part = last_part

    def dumps(self) -> str:
        report = [f"URI={quoted(self.uri)}", f"LAST-MSN={number_to_string(self.last_msn)}"]
        if self.last_part is not None:
            report.append(f"LAST-PART={number_to_string(self.last_part)}")

        return f'#EXT-X-RENDITION-REPORT:{",".join(report)}'

    def __str__(self) -> str:
        return self.dumps()


class RenditionReportList(list, GroupedBasePathMixin):
    def __str__(self) -> str:
        output = [str(report) for report in self]
        return "\n".join(output)


class ServerControl:
    def __init__(
        self, can_skip_until=None, can_block_reload=None, hold_back=None, part_hold_back=None, can_skip_dateranges=None
    ) -> None:
        self.can_skip_until = can_skip_until
        self.can_block_reload = can_block_reload
        self.hold_back = hold_back
        self.part_hold_back = part_hold_back
        self.can_skip_dateranges = can_skip_dateranges

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    def dumps(self) -> str:
        ctrl = []
        if self.can_block_reload:
            ctrl.append(f"CAN-BLOCK-RELOAD={self.can_block_reload}")

        ctrl.extend(
            f"{denormalize_attribute(attr)}={number_to_string(self[attr])}"
            for attr in ["hold_back", "part_hold_back"]
            if self[attr]
        )

        if self.can_skip_until:
            ctrl.append(f"CAN-SKIP-UNTIL={number_to_string(self.can_skip_until)}")
            if self.can_skip_dateranges:
                ctrl.append(f"CAN-SKIP-DATERANGES={self.can_skip_dateranges}")

        return f'#EXT-X-SERVER-CONTROL:{",".join(ctrl)}'

    def __str__(self) -> str:
        return self.dumps()


class Skip:
    def __init__(self, skipped_segments: int, recently_removed_dateranges=None) -> None:
        self.skipped_segments = skipped_segments
        self.recently_removed_dateranges = recently_removed_dateranges

    def dumps(self) -> str:
        skip = [f"SKIPPED-SEGMENTS={number_to_string(self.skipped_segments)}"]
        if self.recently_removed_dateranges is not None:
            skip.append(f"RECENTLY-REMOVED-DATERANGES={quoted(self.recently_removed_dateranges)}")

        return f'#EXT-X-SKIP:{",".join(skip)}'

    def __str__(self) -> str:
        return self.dumps()


class PartInformation:
    __slots__ = ("part_target",)

    def __init__(self, part_target=None) -> None:
        self.part_target = part_target

    def dumps(self) -> str:
        return f"#EXT-X-PART-INF:PART-TARGET={number_to_string(self.part_target)}"

    def __str__(self) -> str:
        return self.dumps()


class PreloadHint(BasePathMixin):
    def __init__(self, type, base_uri, uri, byterange_start=None, byterange_length=None) -> None:  # noqa
        self.hint_type = type
        self.base_uri = base_uri
        self.uri = uri
        self.byterange_start = byterange_start
        self.byterange_length = byterange_length

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    def dumps(self) -> str:
        hint = [f"TYPE={self.hint_type}", f"URI={quoted(self.uri)}"]

        for attr in ["byterange_start", "byterange_length"]:
            if self[attr] is not None:
                hint.append(f"{denormalize_attribute(attr)}={number_to_string(self[attr])}")

        return f'#EXT-X-PRELOAD-HINT:{",".join(hint)}'

    def __str__(self) -> str:
        return self.dumps()


class SessionData:
    def __init__(self, data_id, value=None, uri=None, language=None) -> None:
        self.data_id = data_id
        self.value = value
        self.uri = uri
        self.language = language

    def dumps(self) -> str:
        session_data_out = [f"DATA-ID={quoted(self.data_id)}"]

        if self.value:
            session_data_out.append(f"VALUE={quoted(self.value)}")
        elif self.uri:
            session_data_out.append(f"URI={quoted(self.uri)}")
        if self.language:
            session_data_out.append(f"LANGUAGE={quoted(self.language)}")

        return f'#EXT-X-SESSION-DATA:{",".join(session_data_out)}'

    def __str__(self) -> str:
        return self.dumps()


class DateRangeList(TagList):
    pass


class DateRange:
    def __init__(self, **kwargs: Any) -> None:
        self.id = kwargs["id"]
        self.start_date = kwargs.get("start_date")
        self.class_ = kwargs.get("class")
        self.end_date = kwargs.get("end_date")
        self.duration = kwargs.get("duration")
        self.planned_duration = kwargs.get("planned_duration")
        self.scte35_cmd = kwargs.get("scte35_cmd")
        self.scte35_out = kwargs.get("scte35_out")
        self.scte35_in = kwargs.get("scte35_in")
        self.end_on_next = kwargs.get("end_on_next")
        self.x_client_attrs = [(attr, kwargs.get(attr)) for attr in kwargs if attr.startswith("x_")]

    def dumps(self) -> str:
        daterange = [f"ID={quoted(self.id)}"]

        # whilst START-DATE is technically REQUIRED by the spec, this is
        # contradicted by an example in the same document (see
        # https://tools.ietf.org/html/rfc8216#section-8.10), and also by
        # real-world implementations, so we make it optional here
        if self.start_date:
            daterange.append(f"START-DATE={quoted(self.start_date)}")
        if self.class_:
            daterange.append(f"CLASS={quoted(self.class_)}")
        if self.end_date:
            daterange.append(f"END-DATE={quoted(self.end_date)}")
        if self.duration:
            daterange.append(f"DURATION={number_to_string(self.duration)}")
        if self.planned_duration:
            daterange.append(f"PLANNED-DURATION={number_to_string(self.planned_duration)}")
        if self.scte35_cmd:
            daterange.append(f"SCTE35-CMD={self.scte35_cmd}")
        if self.scte35_out:
            daterange.append(f"SCTE35-OUT={self.scte35_out}")
        if self.scte35_in:
            daterange.append(f"SCTE35-IN={self.scte35_in}")
        if self.end_on_next:
            daterange.append(f"END-ON-NEXT={self.end_on_next}")

        # client attributes sorted alphabetically output order is predictable
        daterange.extend(f"{denormalize_attribute(attr)}={value}" for attr, value in sorted(self.x_client_attrs))

        return f'#EXT-X-DATERANGE:{",".join(daterange)}'

    def __str__(self) -> str:
        return self.dumps()


class ContentSteering(BasePathMixin):
    def __init__(self, base_uri, server_uri, pathway_id=None) -> None:
        self.base_uri = base_uri
        self.uri = server_uri
        self.pathway_id = pathway_id

    def dumps(self) -> str:
        steering = [f"SERVER-URI={quoted(self.uri)}"]

        if self.pathway_id is not None:
            steering.append(f"PATHWAY-ID={quoted(self.pathway_id)}")

        return f'#EXT-X-CONTENT-STEERING:{",".join(steering)}'

    def __str__(self) -> str:
        return self.dumps()


def find_key(keydata, keylist: list[Key]) -> Key | None:
    if not keydata:
        return None
    for key in keylist:
        if key and (
            keydata.get("uri", None) == key.uri
            and keydata.get("method", "NONE") == key.method
            and keydata.get("iv", None) == key.iv
        ):
            return key
    raise KeyError("No key found for key data")


def denormalize_attribute(attribute: str) -> str:
    return attribute.replace("_", "-").upper()


def quoted(string: str) -> str:
    return f'"{string}"'


def number_to_string(number: int | float) -> str:
    with decimal.localcontext() as ctx:
        ctx.prec = 20  # set floating point precision
        d = decimal.Decimal(str(number))
        return f"{d.quantize(decimal.Decimal(1)) if d == d.to_integral_value() else d.normalize()}"
