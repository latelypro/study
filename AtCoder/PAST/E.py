N,Q = map(int, input().split())
result = [['N' for i in range(N)] for j in range(N)]
from pprint import pprint

def follow(follower_id, followee_id):
    result[follower_id][followee_id] = 'Y'

def get_follows(id):
    """
        指定IDユーザーのフォーロリストを返す
    """
    return list(result[id])

def get_followers(id):
    """
        指定IDのユーザーをフォローしているユーザーのidリストを返す
    """
    followers = []
    for user_id in range(N):
        if result[user_id][id] == 'Y':
            followers.append(user_id)
    return followers

for i in range(Q):
    logs = input().split()
    flag = int(logs[0])
    do_user_id = int(logs[1]) - 1
    # ただのフォロー
    if flag == 1:
            target_user_id = int(logs[2]) - 1
            follow(do_user_id, target_user_id)
    # フォロー全返し
    elif flag == 2:
        followers = get_followers(do_user_id)
        for follower_id in followers:
            follow(do_user_id, follower_id)
    # フォローフォロー
    else:
        # ユーザーが現在フォローしている人たち
        follows = get_follows(do_user_id)
        follow_follows = []
        for id, is_follow in enumerate(follows):
            if id != do_user_id and is_follow == 'Y':
                # フォローしている人がフォローしている人たち
                follow_follows.append(get_follows(id))

        for follows in follow_follows:
            for follow_follow_id, is_follow in enumerate(follows):
                if follow_follow_id != do_user_id and is_follow == 'Y':
                    follow(do_user_id, follow_follow_id)


for user_follows in result:
    print(''.join(user_follows))