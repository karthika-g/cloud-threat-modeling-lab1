# Instructor Notes — Lab 1

## Expected failing point

The starter application intentionally contains:

```python
subprocess.run(cmd, shell=True, ...)
```

Bandit should identify this as a shell-injection-related security finding. Bandit is a Python security linter that analyzes source using AST-based checks.

If the Bandit job does not fail because the configured severity threshold is not met in the current tool version, change the workflow inputs to:

```yaml
severity: low
confidence: low
```

The instructional objective is to demonstrate a security gate, not to depend on one exact tool-version message.

## Fix

Replace the command execution with an allowlisted operation rather than executing arbitrary user input through a shell.

One simple training-safe replacement is:

```python
@app.get("/run-check")
def run_check():
    return jsonify(output="training check completed")
```

Then commit and push again.

## Secret exercise

Create a repository secret:

```text
DEMO_API_KEY
```

Suggested training-only value:

```text
training-only-demo-value-123
```

Do not use any real credential.

The workflow passes this secret to the test step through an environment variable. The lab intentionally does not print the value.

## Optional secret-scanning challenge

After the normal pipeline is green, create a temporary file:

```text
training-secret.txt
```

with a fake, non-production value such as:

```text
TRAINING_SECRET_0123456789ABCDEFGHIJKLMNOP
```

Do not use a real credential.

Commit and push it. The objective is to observe the secret-scanning job behavior. Remove the file and push again.

Depending on the Gitleaks rules enabled by the current action release, a made-up training value may or may not match a built-in rule. Do not turn a real credential into the exercise just to force detection.

## Security discussion

Use this attack path:

Developer
  |
  v
Git repository
  |
  v
CI runner
  |
  +--> source code
  +--> dependencies
  +--> secrets
  |
  v
Build artifact
  |
  v
Registry / deployment

Ask participants:
- What happens if source code is malicious?
- What if a dependency is vulnerable?
- What if a CI secret is exposed?
- What if the build artifact is tampered with?
- What permissions should the workflow token have?
- Where should security gates occur?

## Important instructor clarification

A green pipeline does not prove that an application is secure.

The pipeline is providing automated checks against specific classes of known or detectable problems. Threat modeling is still needed to identify architectural threats and abuse paths that automated scanners may not understand.

## Current action/runtime note

This lab uses Gitleaks Action v3. The project documentation notes that v2 used Node 20 and is no longer suitable for GitHub-hosted runners from September 16, 2026; v3 uses the newer runtime.

For production environments, teach participants to pin third-party actions to immutable commit SHAs and review/approve action updates rather than relying indefinitely on mutable major tags.
