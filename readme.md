<p align="center">
<a href="https://www.upsun.com/">
<img src="utils/logo.svg" width="500px">
</a>
</p>

<p align="center">
<a href="https://github.com/platformsh/demo-project/issues">
<img src="https://img.shields.io/github/issues/platformsh/demo-project.svg?style=for-the-badge&labelColor=f4f2f3&color=6046FF&label=Issues" alt="Open issues" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh/demo-project/pulls">
<img src="https://img.shields.io/github/issues-pr/platformsh/demo-project.svg?style=for-the-badge&labelColor=f4f2f3&color=6046FF&label=Pull%20requests" alt="Open PRs" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh/demo-project/blob/main/LICENSE">
<img src="https://img.shields.io/static/v1?label=License&message=MIT&style=for-the-badge&labelColor=f4f2f3&color=6046FF" alt="License" />
</a>&nbsp&nbsp
<br /><br />

<p align="center">
<strong>Contribute, request a feature, or check out our resources</strong>
<br />
<br />
<!-- <a href="https://community.platform.sh"><strong>Join our community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp -->
<a href="https://upsun.com/"><strong>Website</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://upsun.com/features/"><strong>Features</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://docs.upsun.com"><strong>Documentation</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://upsun.com/pricing/"><strong>Pricing</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://upsun.com/blog/"><strong>Blog</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br /><br />
</p>

<h2 align="center">Try the Upsun demo</h2>

## About

This is a simple demo project meant to take users through a product tour of [Upsun](https://upsun.com).

## Getting started

If you already have access to Upsun:

- Visit the Upsun Console (https://console.upsun.com/projects/create-project) to create a new project
- Create or select an organization to run the demo on
- Click **Explore Upsun** to start the demo

## Resume the demo

When you start the demo project through the Upsun console, you will receive all the steps you need to go through the entire demo.
If for some reason you close your browser and lose your place, however, you can pick back up where you left off by following the instructions below.

1. Install the Upsun CLI

    ```bash
    brew install upsun/tap/upsun-cli
    ```

    > [!NOTE]
    > Determine if you already have the CLI installed by running `upsun`.

2. Create a project

    First run, `upsun project:list`.
    If there is _no_ project listed, you can go right ahead back to [https://console.upsun.com/create-project](https://console.upsun.com/create-project) and restart the **Demo project** option.

    If you already created a project, you will find a `PROJECT_ID` associated with that project, which you will use in the next step.

3. Get the demo repository

    > [!NOTE]
    > You can determine if you have already pushed the demo project to Upsun using the command `upsun activity:list --type push`.
    > If you've already pushed code, there will be an entry in the table that says **Your Name pushed to Main**.
    >
    > If you see a `push` activity, run `upsun get PROJECT_ID` to get the code, `cd` the resulting folder, and then move on to step 4.
 
    Get the demo repo by running:

    ```bash
    git clone git@github.com:platformsh/demo-project.git upsun-demo && cd upsun-demo
    ```

    Then push to Upsun

    ```bash
    upsun push -y --set-remote PROJECT_ID
    ```

4. View the environment

    You should be all caught up to resume the demo at this point. 
    Run `upsun url --primary` to view the environment, and visit https://console.upsun.com/projects/PROJECT_ID to view the project.

Welcome to Upsun!

## Contributing

Checkout the [Contributing guide](CONTRIBUTING.md) guide for more details.

### Running this project locally

There is a root package `@platformsh/demo-project` that controls both the backend and frontend app setup.
NPM is required. 

1. `git clone git@github.com:platformsh/demo-project.git`
1. `cd demo-project`
1. `npm install`
1. `npm run start`

These commands will set up everything you need to get started, serving:

- The `backend` Python app from `localhost:8000`
- The `frontend` React app from `localhost:3000`

> [!IMPORTANT]
> If at any time you want to start over, run `npm run clean`.
> This will delete everything you've done in the previous steps.

### Testing individual steps of the demo

When running locally, `npm run start` mimicks the backend connection in `frontend/src/utility/api.ts`.
That is, if you're looking to update steps (defined in `frontend/src/App.tsx`) or commands (defined in `frontend/src/commands.json`)
and view how they will appear to the user, which state is presented is defined in this file. 

In the `fetchEnvironment` method, you will see an `override_state` variable

```jsx
// frontend/src/utility/api.ts

let data;

// If updating the design locally, this variable can help you quickly switch between steps.
//  Note: this value MUST be returned to "default" when pushed to the project repo, or else tests will fail.
// let override_state = "default";
let override_state = "branch"
// let override_state = "redis"
// let override_state = "merge-production"
// let override_state = "scale"
// let override_state = "complete"
```

Changing which state is commented out in this block for the `override_state` variable will allow you to quickly switch between states.

> [!IMPORTANT]
> This switch is included to make design/command changes easy to visualize quickly.
> It is **required** that you reset this variable to `let override_state = "default"` before pushing to the repository.
> If you do not, tests will fail and the PR cannot be accepted.
>
> You can usually tell if forgetting to reset this variable is the reason for failure from the following error message during a test run:
> ```
>  FAIL  src/utility/api.test.tsx
>  ● fetchEnvironment › fetches environment successfully
> ```

### Running tests

This project goes through a number of tests on GitHub that must pass before it can be merged.
These tests are of two types:

1. Code tests
1. Demo path tests

#### Code tests

> [!NOTE]
> You can run all the tests desribed below with the command:
> ```
> ./utils/tests/all.sh
> ```

Before pushing your changes to the repository (or if your PR is failing), please run the following steps locally:

1. Install project dependencies

    ```bash
    npm install
    ```

1. Run backend Python app tests (check for vulnerabilities)

    ```bash
    npm run test:backend
    ```

    > [!NOTE]
    > This test will fail on GitHub if **any** vulnerabilities are found. 

1. Run frontend React tests.

    ```bash
    npm run test:frontend -- --watchAll
    ```

    > [!NOTE]
    > This test will fail on GitHub if **any** React tests fail. 

    Tips:

    - [Make sure that you have returned `override_step` to its previous value](#testing-individual-steps-of-the-demo)
    - Changes to steps in the demo can fundamentally change test expectations. Update tests as you work.

1. Audit frontend dependencies.

    ```bash
    cd frontend && npm audit
    ```

    > [!NOTE]
    > This test will pass on GitHub, so long as there are **no High or Critical vulnerabilities** found.

1. Prettier

    ```bash
    npm run prettier:backend
    npm run prettier:frontend
    npm run lint:frontend
    npm run lint:backend
    ```

    If, for example, you run into the error `[warn] Code style issues found in 3 files. Run Prettier to fix.` for the `frontend`, run `cd frontend && npm run pretty:fix` to fix.

    The workflow on GitHub will fail if this error occurs, so please fix locally when contributing.

#### Demo path tests

_Coming soon_
