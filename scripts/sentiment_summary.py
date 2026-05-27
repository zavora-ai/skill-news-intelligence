#!/usr/bin/env python3
"""Sentiment summary from news data."""
import json,sys
def summarize(data):
    p,neg,neu=data.get("positive",0),data.get("negative",0),data.get("neutral",0)
    tone="positive" if p>60 else "negative" if neg>30 else "mixed"
    return {"tone":tone,"positive":p,"negative":neg,"neutral":neu}
if __name__=="__main__":print(json.dumps(summarize(json.loads(sys.argv[1])),indent=2))
