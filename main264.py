import datetime
from moviepy.editor import *
import os


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
        print(dd)#2021-11-12 21:49:41.011118 2022-07-19 14:31:77.356510
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
                video_time_num_for_sort = int(video_in_list.split('.h264')[0].split('T')[0] +
                                              video_in_list.split('.h264')[0].split('T')[1].split(',')[0] +
                                              video_in_list.split('.h264')[0].split('T')[1].split(',')[1])
                video_in_list_dict_for_sort[video_in_list] = video_time_num_for_sort
        video_order = sorted(video_in_list_dict_for_sort.items(), key=lambda x: x[1], reverse=False)
        return video_order
    return_video_order = find_videos_and_sort(list_of_videos_in_this_dir)
    if return_video_order == -1:
        print("文件定位异常")
        return -1
    print(return_video_order) #order [('20211112T213839,011118.mp4', 20211112213839011118), ('20211112T213909,011118.mp4', 20211112213909011118), ('20211112T213929,011118.mp4', 20211112213929011118)]
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
    if len(return_video_order) == 1 and start_flag == 'start_cls_2': # 特殊情况处理 长度只有一个视频的时候 需要判断一下t1是否大于视频本身的长度 如果不是则以index=0开始剪辑 没有该模块会判断成t1比最晚的视频还要晚
        if (str_time_2_dd(start_time_T1) - datetime.timedelta
                        (seconds=VideoFileClip(return_video_order[0][0]).duration)
                     - str_time_2_dd(return_video_order[-1][0].split('.mp4')[0])).total_seconds() > 0:
            pass # 这里表示t1确实比视频本身还大 会返回0值
        else:
            start_index = 0
            start_flag = 'start_cls_3'
    for tup_video_index in range(len(return_video_order)):
        if end_point > return_video_order[tup_video_index][1]:
            if return_video_order[tup_video_index] == return_video_order[-1] and \
                    (str_time_2_dd(end_time_T2) - datetime.timedelta
                        (seconds=VideoFileClip(return_video_order[tup_video_index][0]).duration)
                     - str_time_2_dd(return_video_order[-1][0].split('.h264')[0])).total_seconds() > 0:
                end_flag = 'end_cls_1'  # t2比最晚的视频还要晚 取最晚的视频整段 并给出提示
                print("T2 比最晚的视频还要晚")
                end_index = tup_video_index
                break
            else:
                end_flag = 'end_cls_3'  # t2在给定的list之中 且非最后一个 取对应index的视频往后加时间到t2
                end_index = tup_video_index
    print(start_flag, end_flag)
    if start_flag == 'start_cls_2':
        print("时间戳异常")
        return -1
    if end_flag == 'end_cls_2':
        print("时间戳异常")
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
        start_point_datetime = return_video_order[start_index][0].split('.h264')[0]
        start_point_datetime_dd = str_time_2_dd(start_point_datetime)
        start_point_diff_sec = (t1 - start_point_datetime_dd).total_seconds()
        clip_start = VideoFileClip(return_video_order[start_index][0])\
            .subclip(start_point_diff_sec, VideoFileClip(return_video_order[start_index][0]).duration)
    elif start_flag == 'start_cls_1':
        clip_start = VideoFileClip(return_video_order[start_index][0])
    if end_flag == 'end_cls_3':
        end_point_datetime = return_video_order[end_index][0].split('.h264')[0]
        end_point_datetime_dd = str_time_2_dd(end_point_datetime)
        end_point_diff_sec = (t2 - end_point_datetime_dd).total_seconds()
        clip_end = VideoFileClip(return_video_order[end_index][0]).subclip(0, end_point_diff_sec)
    elif end_flag == 'end_cls_1':
        clip_end = VideoFileClip(return_video_order[end_index][0])
    if start_index == end_index:
        clip_return = VideoFileClip(return_video_order[end_index][0]).subclip(start_point_diff_sec, end_point_diff_sec)
    if start_index < end_index:
        data_list.append(clip_start)
        for i in range(start_index+1, end_index):
            data_list.append(VideoFileClip(return_video_order[start_index+i][0]))
        data_list.append(clip_end)
        clip_return = concatenate_videoclips(data_list, method='compose')

    # video_length_time = VideoFileClip("20211112T213909,011118.mp4").duration
    # print(video_length_time)
    # video = VideoFileClip("yt1s.com - The Cup Song  Youtube Covers Mix_v720P.mp4").
    # str = '20211112T213839,011118'  # 剪辑到秒的小数点后两位
    # video = VideoFileClip("yt1s.com - The Cup Song  Youtube Covers Mix_v720P.mp4").subclip(10, 40)
    clip_return.write_videofile(start_time_T1 + ".mp4")



list_of_videos_in_this_dir_for_test = ['20220719T143157,356510.h264']
T1 = '20220719T143157,356510'
T2 = '20220719T143159,356510'
extract_a_seg_from_list_of_videos(T1, T2, list_of_videos_in_this_dir_for_test)
# video = VideoFileClip("yt1s.com - The Cup Song  Youtube Covers Mix_v720P.mp4").subclip(10, 40.123121)
# video.write_videofile("done.mp4")
