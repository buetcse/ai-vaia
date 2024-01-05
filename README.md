# ai-vaia
AI Vaia


## Release V1
Barebone proof of concept idea

A cron running daily and posting to "AI Vaia" Facebook page.
The contents needed to be taken from 

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
