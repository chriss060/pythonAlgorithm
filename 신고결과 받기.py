# 프로그래머스 1: 신고 결과 받기
from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)

    user_list_report = defaultdict(set)
    num_reported = defaultdict(int)
    suspended = []

    for r in report:
        reporter, reportee = r.split()

        num_reported[reportee] += 1
        user_list_report[reporter].add(reportee)

        if num_reported[reportee] == k:
            suspended.append(reportee)

    for s in suspended:
        for i in range(len(id_list)):
            if s in user_list_report[id_list[i]]:
                answer[i] += 1

    return answer