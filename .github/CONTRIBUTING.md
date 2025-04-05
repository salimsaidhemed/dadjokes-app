# Contributing to DadJokes App

We welcome contributions to the DadJokes App! Please follow these guidelines to ensure a smooth collaboration.

## Branching Strategy

We use the **Git Flow** branching model. Here's how you can contribute:

1. **Main Branch**: The `main` branch contains production-ready code. Do not commit directly to this branch.
2. **Develop Branch**: The `develop` branch is the integration branch for features and fixes. All feature branches should branch off from `develop`.

## Workflow

1. **Fork the Repository**: Create a fork of the repository to your GitHub account.
2. **Clone the Repository**: Clone your fork to your local machine.
    ```bash
    git clone https://github.com/your-username/dadjokes-app.git
    ```
3. **Create a Feature Branch**: Use the following naming convention:
    - Features: `feature/<short-description>`
    - Bug Fixes: `bugfix/<short-description>`
    - Hotfixes: `hotfix/<short-description>`
    ```bash
    git checkout -b feature/awesome-feature develop
    ```
4. **Commit Changes**: Write clear and concise commit messages.
    ```bash
    git commit -m "Add awesome feature"
    ```
5. **Push to Your Fork**: Push your branch to your forked repository.
    ```bash
    git push origin feature/awesome-feature
    ```
6. **Create a Pull Request**: Open a pull request (PR) to the `develop` branch. Provide a detailed description of your changes.

## Code Guidelines

- Follow the coding style used in the project.
- Write tests for new features or bug fixes.
- Ensure all tests pass before submitting a PR.

## Reviewing and Merging

- PRs will be reviewed by maintainers.
- Once approved, your changes will be merged into `develop`.
- Releases to `main` will be handled by maintainers.

Thank you for contributing!  