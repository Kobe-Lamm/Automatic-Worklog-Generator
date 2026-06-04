from summarizer import summarize_session
import json

# extract the sessions we 
with open("data/session.json") as f:
    sessions = json.load(f)
    
# Store into summaries array
summaries = []

# Summarize the sessions:
for session in sessions:
    summaries.append(summarize_session(session))

    
# Create daily summaries based on session summaries
def create_daily_summaries (summaries):
    report = {
        "work_completed": [],
        "session_count": len(summaries)
    }
    for summary in summaries:
        report["work_completed"].append(summary)
    return report

# Create the report
report = create_daily_summaries(summaries)

# 
with open("reports/daily_summary.json", "w") as f: 
    json.dump(f)
print(report)
    

print(summaries)