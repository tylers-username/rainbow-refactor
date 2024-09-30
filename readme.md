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
1. Install required packages: `poetry install`
1. Make TailwindCSS CLI available: `poetry run download-tailwind`
1. Run TailwindCSS file watcher: `poetry run dev-css-watch`
1. Run livereload server: `poetry run app-serve-livereload` 

### Testing individual steps of the demo

When running locally, you can use the `.env` (copied from `.env.sample`) to update the variables used to detect which 
steps have been completed. `PLATFORM_ENVIRONMENT_TYPE` will switch between `production` and `staging`.

For now, to emulate Redis being configured in Upsun there are two options:

1. Recreate the `PLATFORM_RELATIONSHIPS` variable.
2. Or, update `upsun_demo_app/routes.py:22` from `"has_redis_service": has_redis_service(),` to `"has_redis_service": True,`

> [!IMPORTANT]
> You must manually restart the local server if `.env`, `main.py` or `routes.py` are updated.

### Running tests

[TBD]

#### Code tests

[TBD]

Before pushing your changes to the repository (or if your PR is failing), please run the following steps locally:

1. Install project dependencies

    ```bash
    poetry install
    ```

1. Run app tests (check for vulnerabilities)

    [TBD]

1. Audit frontend dependencies.

    ```bash
    poetry run app_audit
    ```

1. Prettier

    ```bash
    poetry run app_prettier
    poetry run app_lint
    ```

    `app_prettier` triggers `poetry run black . --check` which will only check for issues. If you wish to apply 
    recommendations you may use `poetry run black .`

#### Demo path tests

_Coming soon_
