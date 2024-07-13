from typing import TypeVar

from speech_utils.audio_segmentation_utils.non_overlapping_segments import NeNoSegments
from speech_utils.audio_segmentation_utils.ordered_spans import OrderedSpans
from speech_utils.data_models.time_spans import TimeSpan

TTimeSpan_co = TypeVar("TTimeSpan_co", bound=TimeSpan, covariant=True)


def merge_close_and_short_or_overlapping_segments(
    # both are ordered
    segments: OrderedSpans[TTimeSpan_co] | NeNoSegments[TTimeSpan_co],
    # TODO: higher-level (generic) type-vars not really possible in python: https://stackoverflow.com/questions/54118095/how-to-use-generic-higher-level-type-variables-in-type-hinting-system
    # hardcoded NeNoSegments, cause cannot make thise generic -> TNeNoSegments[TTimeSpan_co] does not work in python!
    max_gap_dur: float = 0.2,
    # gap within between two segments -> shorter than this gets merged
    min_seg_dur: float | None = None,
    # close segments only get merged if at least one is shorter than this
) -> NeNoSegments[TTimeSpan_co]:
    """
    example of "how to lose" type information
    does parsing in the sense of merging segments but the output is a Sequence that does not hold any information about the merging!
    """
    # formerly called: "merge_segments"
    exp_segs: list[TTimeSpan_co] = [segments[0]]
    for seg in segments[1:]:
        previous = exp_segs[-1]
        is_close = seg.start - previous.end < max_gap_dur
        if min_seg_dur is None:
            is_mergable = is_close
        else:
            one_is_short = (
                seg.end - seg.start < min_seg_dur
                or previous.end - previous.start < min_seg_dur
            )
            is_overlapping = seg.start < previous.end
            is_mergable = (is_close and one_is_short) or is_overlapping

        if is_mergable:
            exp_segs[-1] = previous.merge(previous, seg)
        else:
            exp_segs.append(seg)

    return NeNoSegments[TTimeSpan_co].create_without_validation(exp_segs)
