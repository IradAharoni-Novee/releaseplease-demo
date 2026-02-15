# releaseplease-demo

A minimal demo of a release-please-driven deployment flow.

## Included workflows
- `release-please.yml`: creates/updates release PRs and triggers staging/prod promotions after release creation.
- `deploy-dev-preview.yml`: on `deploy-dev` PR label, computes a semver-compatible dev tag and opens a dev promotion PR.
- `promote-environment.yml`: creates promotion PRs for `dev`, `staging`, or `prod` by updating `environments/<env>.json`.
- `semantic-pr-title.yml`: enforces conventional PR titles.

## Tag formats
- Release: `vX.Y.Z`
- Dev preview: `v<base>-dev.<pr>.sha.<shortsha>`
