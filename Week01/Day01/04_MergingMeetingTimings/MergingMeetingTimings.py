def MergingMeetingTimings(meetings):
    i_length=len(i_array)
    if (i_length<2):
        return meetings
    meetings.sort()
    result=[meetings[0]]
    for curr_m_start,curr_m_end in meetings[1:]:
        prev_m_start,prev_m_end=result[-1]
        if (curr_m_start <= prev_m_end):
            result[-1] = (prev_m_start,max(prev_m_end,curr_m_end))
        else:
            result.append((curr_m_start, curr_m_end))
    return result


i_array=[]
print("i_array",i_array)
print(MergingMeetingTimings(i_array))
print("#######################")

i_array=[(1, 10), (2, 6), (3, 5), (7, 9)]
print("i_array",i_array)
print(MergingMeetingTimings(i_array))
print("#######################")

i_array=[(1, 10), (10, 16)]
print("i_array",i_array)
print(MergingMeetingTimings(i_array))
print("#######################")

i_array=[(1, 10)]
print("i_array",i_array)
print(MergingMeetingTimings(i_array))
print("#######################")