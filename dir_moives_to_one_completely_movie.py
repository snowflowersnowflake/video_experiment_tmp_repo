import datetime

from moviepy.editor import *
import os
import time


# def rename_the_seg_in_the_list_of_videos(list_of_videos_in_this_dir):
#     """
#     :param list_of_videos_in_this_dir: the input files which should be contained in this root dir
#     :return: save renamed data in a file with filename from the first video
#     """
#
#     def str_time_2_dd(str_with_file):
#         """
#         :param str_with_file: filename str
#         :return: datetime about filename
#         """
#         date = str_with_file.split('T')[0]
#         time = str_with_file.split('T')[1]
#         time_high = time.split(',')[0]
#         time_low = time.split(',')[1]
#         format_year = date[:4]
#         format_mon = date[4:6]
#         format_days = date[6:8]
#         format_hh = time_high[:2]
#         format_mm = time_high[2:4]
#         # format_ss
#         format_ss = time_high[4:6] + '.' + time_low
#         dd = format_year + '-' + format_mon + '-' + format_days + ' ' + format_hh + ':' + format_mm + ':' + format_ss
#         # print(dd)
#         # time.sleep(10)
#         dd = datetime.datetime.strptime(dd, "%Y-%m-%d %H:%M:%S.%f")
#         return dd
#
#     def find_videos_and_sort(find_list_of_videos_in_this_dir):
#         """
#         :param find_list_of_videos_in_this_dir:
#         :return: if in dir and sort
#         """
#
#         # check dir
#         def get_files_from_dir(from_dir):
#             if not os.path.exists(from_dir):
#                 return ''
#             file_paths = []
#             for root, directories, files in os.walk(from_dir):
#                 for filename in files:
#                     filepath = os.path.join(root, filename)
#                     file_paths.append(filepath)
#             return file_paths
#
#         all_file_in_this_dir = get_files_from_dir('./')
#         video_in_list_dict_for_sort = {}
#         for video_in_list in find_list_of_videos_in_this_dir:
#             if ('./' + video_in_list) not in all_file_in_this_dir:
#                 print("文件名：", video_in_list, " 该文件不存在于当前目录下,请检查")
#                 return -1
#             else:
#                 video_time_num_for_sort = int(video_in_list.split('.mp4')[0].split('T')[0] +
#                                               video_in_list.split('.mp4')[0].split('T')[1].split(',')[0] +
#                                               video_in_list.split('.mp4')[0].split('T')[1].split(',')[1])
#                 video_in_list_dict_for_sort[video_in_list] = video_time_num_for_sort
#         video_order = sorted(video_in_list_dict_for_sort.items(), key=lambda x: x[1], reverse=False)
#         return video_order
#
#     return_video_order = find_videos_and_sort(list_of_videos_in_this_dir)
#     if return_video_order == -1:
#         print("文件定位异常")
#         return -1
#     print("order", return_video_order)
    # time.sleep()


def extract_a_seg_from_list_of_videos(start_time_T1, end_time_T2, list_of_videos_in_this_dir):
    """
    :param start_time_T1:  output file start T1
    :param end_time_T2:    output file end T2
    :param list_of_videos_in_this_dir: the input files which should be contained in this root dir
    :return: generate a combined output video file with target datetime
    """

    def str_time_2_dd(str_with_file):
        """
        :param str_with_file: filename str
        :return: datetime about filename
        """
        date = str_with_file.split('T')[0]
        time = str_with_file.split('T')[1]
        time_high = time.split(',')[0]
        time_low = time.split(',')[1]
        format_year = date[:4]
        format_mon = date[4:6]
        format_days = date[6:8]
        format_hh = time_high[:2]
        format_mm = time_high[2:4]
        # format_ss
        format_ss = time_high[4:6] + '.' + time_low
        dd = format_year + '-' + format_mon + '-' + format_days + ' ' + format_hh + ':' + format_mm + ':' + format_ss
        # print(dd)
        # time.sleep(10)
        dd = datetime.datetime.strptime(dd, "%Y-%m-%d %H:%M:%S.%f")
        return dd

    def find_videos_and_sort(find_list_of_videos_in_this_dir):
        """
        :param find_list_of_videos_in_this_dir:
        :return: if in dir and sort
        """

        # check dir
        def get_files_from_dir(from_dir):
            if not os.path.exists(from_dir):
                return ''
            file_paths = []
            for root, directories, files in os.walk(from_dir):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)
            return file_paths

        all_file_in_this_dir = get_files_from_dir('./')
        video_in_list_dict_for_sort = {}
        for video_in_list in find_list_of_videos_in_this_dir:
            if ('./' + video_in_list) not in all_file_in_this_dir:
                print("文件名：", video_in_list, " 该文件不存在于当前目录下,请检查")
                return -1
            else:
                video_time_num_for_sort = int(video_in_list.split('.mp4')[0].split('T')[0] +
                                              video_in_list.split('.mp4')[0].split('T')[1].split(',')[0] +
                                              video_in_list.split('.mp4')[0].split('T')[1].split(',')[1])
                video_in_list_dict_for_sort[video_in_list] = video_time_num_for_sort
        video_order = sorted(video_in_list_dict_for_sort.items(), key=lambda x: x[1], reverse=False)
        return video_order

    return_video_order = find_videos_and_sort(list_of_videos_in_this_dir)
    if return_video_order == -1:
        print("文件定位异常")
        return -1
    print("order", return_video_order)
    # time.sleep()
    start_point = int(start_time_T1.split('T')[0] + start_time_T1.split('T')[1].split(',')[0] +
                      start_time_T1.split('T')[1].split(',')[1])
    end_point = int(end_time_T2.split('T')[0] + end_time_T2.split('T')[1].split(',')[0] +
                    end_time_T2.split('T')[1].split(',')[1])
    start_flag = '0'  # init
    end_flag = '0'
    start_index = 0
    end_index = 0
    start_flag = 'start_cls_2'  # t1比最晚的视频还要晚 无结果 输出时间戳异常
    end_flag = 'end_cls_2'  # t2比最早的视频还要早 无结果 输出时间戳异常
    for tup_video_index in range(len(return_video_order)):
        # print("here",start_point,return_video_order[tup_video_index][1])
        if start_point < return_video_order[tup_video_index][1]:
            if return_video_order[tup_video_index] == return_video_order[0]:
                start_flag = 'start_cls_1'  # t1比最早的视频还早 取最早的视频整段 并给出提示
                print("T1 比最早的视频还要早")
                start_index = 0
                break
            else:
                start_flag = 'start_cls_3'  # t1在给定的list中 且非最开始一个 取对应index-1的视频往后加时间到t1
                start_index = tup_video_index - 1
                break
    if len(return_video_order) == 1 and start_flag == 'start_cls_2':
        # 特殊情况处理 长度只有一个视频的时候 需要判断一下t1是否大于视频本身的长度 如果不是则以index=0开始剪辑 没有该模块会判断成t1比最晚的视频还要晚
        if (str_time_2_dd(start_time_T1) - datetime.timedelta
            (seconds=VideoFileClip(return_video_order[0][0]).duration)
            - str_time_2_dd(return_video_order[-1][0].split('.mp4')[0])).total_seconds() > 0:
            pass  # 这里表示t1确实比视频本身还大 会返回0值
        else:
            start_index = 0
            start_flag = 'start_cls_3'

    for tup_video_index in range(len(return_video_order)):
        if end_point > return_video_order[tup_video_index][1]:
            if return_video_order[tup_video_index] == return_video_order[-1] and \
                    (str_time_2_dd(end_time_T2) - datetime.timedelta
                        (seconds=VideoFileClip(return_video_order[tup_video_index][0]).duration)
                     - str_time_2_dd(return_video_order[-1][0].split('.mp4')[0])).total_seconds() > 0:
                end_flag = 'end_cls_1'  # t2比最晚的视频还要晚 取最晚的视频整段 并给出提示
                print("T2 比最晚的视频还要晚")
                end_index = tup_video_index
                break
            else:
                end_flag = 'end_cls_3'  # t2在给定的list之中 且非最后一个 取对应index的视频往后加时间到t2
                end_index = tup_video_index
    print(start_flag, end_flag)
    if start_flag == 'start_cls_2':
        print(" start_cls_2 时间戳异常")
        return -1
    if end_flag == 'end_cls_2':
        print(" end_cls_2 时间戳异常")
        return -1
    # print("st index", start_index)
    t1 = str_time_2_dd(start_time_T1)
    t2 = str_time_2_dd(end_time_T2)
    start_point_diff_sec = 0
    end_point_diff_sec = 0
    clip_start = None
    clip_end = None
    clip_return = None
    data_list = []
    if t1 > t2:
        print("t1>t2 时间戳异常")
        return -1
    if start_flag == 'start_cls_3':
        start_point_datetime = return_video_order[start_index][0].split('.mp4')[0]
        start_point_datetime_dd = str_time_2_dd(start_point_datetime)
        start_point_diff_sec = (t1 - start_point_datetime_dd).total_seconds()
        clip_start = VideoFileClip(return_video_order[start_index][0]) \
            .subclip(start_point_diff_sec, VideoFileClip(return_video_order[start_index][0]).duration)
    elif start_flag == 'start_cls_1':
        clip_start = VideoFileClip(return_video_order[start_index][0])
    if end_flag == 'end_cls_3':
        end_point_datetime = return_video_order[end_index][0].split('.mp4')[0]
        end_point_datetime_dd = str_time_2_dd(end_point_datetime)
        end_point_diff_sec = (t2 - end_point_datetime_dd).total_seconds()
        clip_end = VideoFileClip(return_video_order[end_index][0]).subclip(0, end_point_diff_sec)
    elif end_flag == 'end_cls_1':
        clip_end = VideoFileClip(return_video_order[end_index][0])
    if start_index == end_index:
        if start_flag == 'start_cls_3' and end_flag == 'end_cls_3':
            clip_return = VideoFileClip(return_video_order[end_index][0]).subclip(start_point_diff_sec,
                                                                                  end_point_diff_sec)
        elif start_flag == 'start_cls_1' and end_flag == 'end_cls_3':
            clip_return = clip_end
        elif start_flag == 'start_cls_3' and end_flag == 'end_cls_1':
            clip_return = clip_start
    if start_index < end_index:
        data_list.append(clip_start)
        for i in range(start_index + 1, end_index):
            data_list.append(VideoFileClip(return_video_order[start_index + i][0]))
        data_list.append(clip_end)
        clip_return = concatenate_videoclips(data_list, method='compose')

    # video_length_time = VideoFileClip("20211112T213909,011118.mp4").duration
    # print(video_length_time)
    # video = VideoFileClip("yt1s.com - The Cup Song  Youtube Covers Mix_v720P.mp4").
    # str = '20211112T213839,011118'  # 剪辑到秒的小数点后两位
    # video = VideoFileClip("yt1s.com - The Cup Song  Youtube Covers Mix_v720P.mp4").subclip(10, 40)
    clip_return.write_videofile('./save/'+ start_time_T1 + ".mp4")


# list_of_videos_in_this_dir_for_test = ['20211112T213839,011118.mp4' ]
# T1 = '20211112T213839,011119'
# T2 = '20211112T213849,011118'
# extract_a_seg_from_list_of_videos(T1, T2, list_of_videos_in_this_dir_for_test)
# video = VideoFileClip("yt1s.com - The Cup Song  Youtube Covers Mix_v720P.mp4").subclip(10, 40.123121)
# video.write_videofile("done.mp4")


def str_time_2_dd(str_with_file):
    """
    :param str_with_file: filename str
    :return: datetime about filename
    """
    date = str_with_file.split('T')[0]
    time = str_with_file.split('T')[1]
    time_high = time.split(',')[0]
    time_low = time.split(',')[1]
    format_year = date[:4]
    format_mon = date[4:6]
    format_days = date[6:8]
    format_hh = time_high[:2]
    format_mm = time_high[2:4]
    # format_ss
    format_ss = time_high[4:6] + '.' + time_low
    dd = format_year + '-' + format_mon + '-' + format_days + ' ' + format_hh + ':' + format_mm + ':' + format_ss
    # print(dd)
    # time.sleep(10)
    dd = datetime.datetime.strptime(dd, "%Y-%m-%d %H:%M:%S.%f")
    return dd


def dd_2_str_time(dd_with_file):
    """
    :param str_with_file: filename dd
    :return: ori str filename
    """
    str_dd = dd_with_file.strftime("%Y%m%dT%H%M%S,%f") + '.mp4'
    return str_dd

def combine_the_filenames_in_root_dir_to_a_whole_list(root_path='./'):
    """first for quickly proc the work, use these code to combine the filenames in root dir to a whole list"""
    """
    :return: a list with .mp4
    """

    # check dir with mp4
    def get_files_from_dir_with_mp4(from_dir):
        if not os.path.exists(from_dir):
            return ''
        file_paths = []
        for root, directories, files in os.walk(from_dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                if filepath.endswith('.mp4'):
                    file_paths.append(filepath)
        return file_paths

    root_list_mp4 = get_files_from_dir_with_mp4(root_path)
    return root_list_mp4

def rename_and_cal_the_start_time_of_before_and_motion():
    """
    :return: None; rename the mp4 in root
    """
    # check dir
    def get_files_from_dir(from_dir='./'):
        if not os.path.exists(from_dir):
            return ''
        file_paths = []
        for root, directories, files in os.walk(from_dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    all_files_from_dir = get_files_from_dir()
    print(all_files_from_dir)
    mp4_lists = combine_the_filenames_in_root_dir_to_a_whole_list()
    print(mp4_lists)
    # os.rename('fuben.mp4.mp4', "fubbb.mp4")
    # os.rename('./video-20220719T012228,393973-before.mp4',  'foo.mp4')
    for mp4 in mp4_lists:
        split_name_mp4 = mp4.split('.mp')[0].split('./')[1]
        if split_name_mp4.endswith('before'):  # video-20220719T012228,393973-before...
            time_name_mp4 = split_name_mp4.split('video-')[1].split('-before')[0]
            split_name_mp4_path = split_name_mp4 + '.mp4'
            print(split_name_mp4_path)
            clip = VideoFileClip(split_name_mp4_path)
            dur = clip.duration
            dd_dur = datetime.timedelta(seconds=dur)
            # print(dd_dur)
            dd_mp4 = str_time_2_dd(time_name_mp4)
            new_dd_mp4_before = dd_mp4 - dd_dur
            str_new_dd_mp4_before = dd_2_str_time(new_dd_mp4_before)
            clip.close()
            if "./" + str_new_dd_mp4_before in all_files_from_dir:  # 重命名的时候check一下目录会不会冲突
                print('./' + str_new_dd_mp4_before, "这个文件名已经存在于目录之中，系统进行修改")
                os.rename('./' + split_name_mp4_path, "./" + 'same-rename-' + str_new_dd_mp4_before)
            elif "./" + str_new_dd_mp4_before not in all_files_from_dir:
                os.rename('./' + split_name_mp4_path, "./" + str_new_dd_mp4_before)
                print('./' + str_new_dd_mp4_before, "已经对其重命名")

        if split_name_mp4.endswith('motion'):
            # print(split_name_mp4)
            time_name_mp4 = split_name_mp4.split('video-')[1].split('-motion')[0] + '.mp4'  # rename
            split_name_mp4_path = split_name_mp4 + '.mp4'
            # print(time_name_mp4)
            if "./" + time_name_mp4 in all_files_from_dir:  # 重命名的时候check一下目录会不会冲突
                print('./' + time_name_mp4, "这个文件名已经存在于目录之中，系统进行修改")
                os.rename('./' + split_name_mp4_path, "./" + 'same-rename-' + time_name_mp4)
            elif "./" + time_name_mp4 not in all_files_from_dir:
                os.rename('./' + split_name_mp4_path, "./" + time_name_mp4)
                print('./' + time_name_mp4, "已经对其重命名")


# rename_and_cal_the_start_time_of_before_and_motion()  # it may rename the files

def extract_a_seg_from_list_of_videos_of_root_consider_interval(root = './'):
    group_seg_list = [ ]
    # first cal the continuous seg. and append stop point in different segs
    stop_point = []
    last_interval = 0
    index_cnt = 0
    mp4_lists = combine_the_filenames_in_root_dir_to_a_whole_list()
    mp4_lists_sorted = []
    # mp4_lists it must be sorted by time
    video_in_list_dict_for_sort = {}
    for video_in_list in mp4_lists:
        video_in_list = video_in_list.split('./')[1]
        video_time_num_for_sort = int(video_in_list.split('.mp4')[0].split('T')[0] +
                                      video_in_list.split('.mp4')[0].split('T')[1].split(',')[0] +
                                      video_in_list.split('.mp4')[0].split('T')[1].split(',')[1])
        video_in_list_dict_for_sort[video_in_list] = video_time_num_for_sort
    video_order = sorted(video_in_list_dict_for_sort.items(), key=lambda x: x[1], reverse=False)
    for x in video_order:
        mp4_lists_sorted.append(x[0])
    for mp4 in mp4_lists_sorted:
        if index_cnt != len(mp4_lists_sorted) - 1:
            clip = VideoFileClip(mp4)
            dur = clip.duration
            dd_dur = datetime.timedelta(seconds=dur)
            dd_mp4 = str_time_2_dd(mp4.split('.mp')[0])
            new_dd = dd_mp4 + dd_dur
            next_dd = str_time_2_dd(mp4_lists_sorted[index_cnt+1].split('.mp')[0])
            if (next_dd - new_dd).total_seconds() > 1:
                stop_point.append(index_cnt + 1) # +1 为了方便后面处理分割 因为list左闭右开
            index_cnt += 1
            clip.close()
    print(stop_point)
    for stp in stop_point:
        group_seg_list.append(mp4_lists_sorted[last_interval:stp])
        last_interval = stp
    group_seg_list.append(mp4_lists_sorted[stop_point[-1]:])
    print(group_seg_list)
    # then make every group to whole movie
    for group in group_seg_list:
        T1 =  str_time_2_dd(group[0].split('.mp')[0]) - datetime.timedelta(microseconds=1)
        groupmp4 = group[-1]
        clip = VideoFileClip(groupmp4)
        dur = clip.duration
        dd_dur = datetime.timedelta(seconds=dur)
        dd_mp4 = str_time_2_dd(groupmp4.split('.mp')[0])
        new_dd = dd_mp4 + dd_dur
        T2 = new_dd + datetime.timedelta(microseconds=1)
        T1 = dd_2_str_time(T1).split('.mp')[0]
        T2 = dd_2_str_time(T2).split('.mp')[0]
        # print(T1, T2)
        extract_a_seg_from_list_of_videos(T1,T2,group)



extract_a_seg_from_list_of_videos_of_root_consider_interval()