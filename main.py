import json

import httpx


def read_messages_from_id(id):
    request = httpx.post("no more url",
                         json={"params": {
                             "ProfileID": id,
                             "Current_ProfileID": id,
                             "Search_Term": "",
                             "Row_PerPage": 999,
                             "Page_Number": 1,
                             "Filter_Not_Viewed": False,
                             "Filter_Sent": False
                         }})
    return request


def get_student_id_from_messages(j_son, id):
    print(j_son.content.decode().replace("\\", ""))

    for msg in j_son.content.decode().replace("\\", "").replace("{\"d\":\"[{", "").split("},{"):
        try:
            newmsg = json.loads("{" + msg + "}")
            print(newmsg)
            if len(newmsg) < 7:
                continue
            if str(newmsg["AUTHOR_PROFILE_ID"]).__contains__(str(id)):
                print(newmsg["AUTHOR_PEOPLE_ID"], "aopdkapiowdj")
                return newmsg["AUTHOR_PEOPLE_ID"]
        except(Exception):
            print("NO WORKY + \n")
            continue

    return None


def send_message(from_id, to_id, content):
    people_id = get_student_id_from_messages(read_messages_from_id(to_id), to_id)

    if str(people_id) is not None:
        request = httpx.post("no more url", json={
            "msg": {
                "ASSIGNMENT_PEOPLE_ID": 0,
                "ActivityGroupingId": 0,
                "ActivityTypeId": 0,
                "AssignmentGroupingId": "0",
                "AuthorId": from_id,
                "ClassId": 0,
                "FeedbackTeacherId": 0,
                "GroupId": 0,
                "HasStudentFeedback": False,
                "Link": "",
                "Message": content,
                "NeedHelp": False,
                "RecepientId": to_id,
                "RecipientClasses": ",",
                "RecipientGroups": ",",
                "RecipientPeople": "," + str(people_id) + ",",
                "SocialCircleId": 0,
                "SocialMessageTypeId": 5,
                "StandardId": 0,
                "StandardName": "",
                "StepNumber": 0,
                "StudentPeopleId": 0,
                "TaskId": 0
            }
        })
        return request


if __name__ == '__main__':
    print(send_message(1234567890, 1234567890, "Hello").content)
