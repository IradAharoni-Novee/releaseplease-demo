# releaseplease-demo

A minimal demo of a release-please-driven deployment flow.

## Included workflows
- `release-please.yml`: creates/updates release PRs and triggers staging/prod promotions after release creation.
- `promote-environment.yml`: creates promotion PRs for `staging` or `prod` by updating `environments/<env>.json`.
- `semantic-pr-title.yml`: enforces conventional PR titles.

## Tag formats
- Release: `vX.Y.Z`
