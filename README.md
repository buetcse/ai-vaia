# ai-vaia
AI Vaia


## Release V1
Barebone proof of concept idea

A cron running daily and scheduling to "AI Vaia" Facebook page. The schedule should be 7 days later. 

**Concerns**
* Simple script and less deployment dependency
* Barebone pipeline to test the automatic posting idea via bots
* With next week schedule, we can go to facebook page and see upcoming schedueld posts and do manual verification. This will reduce our initial effort of building approval infrastructure.

**Control Flow**

```mermaid
flowchart TB
    A[Cron Scheduler] -->|trigger| B[Start]
    C[User] -->|cmd line| B
    B -->|get the story idea| D[Open AI Api]
    B -->|script for the idea| D[Open AI Api]
    B -->|images for each lines| D[Open AI Api]
    B -->|images for each lines| E[TTS Engine]
    B -->|genereates video| F[Video Maker]
    B -->|schedule posts| G[Facebook Meta API]
```


## Release V2
Campaign Manager
