import json
import re

def json_msg_to_text(j):
    if "edited_timestamp" in j and j["edited_timestamp"] is not None:
        e = "[{} edited {}] {}#{}: {}".format(
            j["timestamp"],
            j["edited_timestamp"],
            j["author_name"],
            j["author_discrim"],
            j["content"])
    else:
        e = "[{}] {}#{}: {}".format(
            j["timestamp"],
            j["author_name"],
            j["author_discrim"],
            j["content"])
    if "attachments" in j:
        for a in j["attachments"]:
            e += "\nATTACHMENT: " + a
    return e

def json_file_to_string(fn):
    with open(fn) as fi:
        j = json.load(fi)
    # time to comprehend lists
    return "\n\n\n".join([
        re.sub(r"(\n){2,}", "\n\n",
            (("\n".join([json_msg_to_text(m) for m in e["messages"]]))
                if e["is_quote"]
                else json_msg_to_text(e)))
        for e in j])

def json_file_to_html_array(fn):
    with open(fn) as fi:
        j = json.load(fi)
    m = []
    for e in j:
        m.append(re.sub(r"(\n){2,}", "\n\n",
                (("\n".join([json_msg_to_text(m) for m in e["messages"]]))
                    if e["is_quote"]
                    else json_msg_to_text(e))).replace("\n", "&lt;br /&gt;"))
    return m
