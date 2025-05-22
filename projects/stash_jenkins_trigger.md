# Stash/Bitbucket + Jenkins tips

## Using [Http Request Post Receive Hook] and [Build Authorization Token Root Plugin]

The notifications did not work for me because of 
```org.acegisecurity.AccessDeniedException: Invalid token provided.```
Instead

```http://{JENKINS_URL}/buildByToken/build?job={SOME+JOB+NAME}&token={TOKEN}/```

use

```http://{JENKINS_URL}/buildByToken/build?token={TOKEN}&job={SOME+JOB+NAME}/```

Fixed! Bitbucket can now trigger jenkins build!
