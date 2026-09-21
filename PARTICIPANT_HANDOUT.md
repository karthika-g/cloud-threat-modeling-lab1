# Participant Handout — Lab 1

## Scenario

You are part of a cloud engineering team building a small Python web service.

The company wants every change to pass automated security checks before it can be treated as a releasable artifact.

You will implement a pipeline that checks:

1. Application tests
2. Static Application Security Testing (SAST)
3. Dependency vulnerabilities
4. Hardcoded secrets
5. Build artifact creation

## Definition of done

- [ ] Code is in a GitHub repository.
- [ ] GitHub Actions runs automatically.
- [ ] Tests execute successfully.
- [ ] A repository secret is configured.
- [ ] Bandit scans the application.
- [ ] pip-audit scans dependencies.
- [ ] Gitleaks scans the repository.
- [ ] A build artifact is uploaded.
- [ ] You have seen a security gate fail.
- [ ] You fixed the issue.
- [ ] The final pipeline is green.

## Security mindset

For every pipeline stage, ask:

> What attack does this control reduce?

> What does this control NOT detect?

> What happens if the control itself is compromised?

> What permissions does the pipeline identity have?

## Final reflection

Draw this before leaving the lab:

```text
Developer
   |
   v
Git
   |
   v
CI
   |
   +--> SAST
   +--> Dependency Scan
   +--> Secret Scan
   |
   v
Artifact
   |
   v
Deployment
```

Mark at least three trust boundaries and three assets.
