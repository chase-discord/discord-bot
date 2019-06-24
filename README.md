# Chase Discord Bot
A Discord bot for use on the Chase Discord server

## Production

This bot is automatically built and run from the `master` branch and will automatically update once changes have been committed.

## Development

### Using pipenv

All of the bot's dependencies are managed by `pipenv`, this makes a virtual environement for the bot allowing it to have the same dependencies and Python version installed no matter what it is running on.

```bash
curl https://pyenv.run | bash # Optionally install pyenv to install the recommended version of Python automatically
python3 -m pip install --user pipenv
```

Now clone the repository to your computer and install the dependencies.

```bash
pipenv install
```

Now that the dependencies have been installed, we need to set the Discord bot token (take a look [here](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) if you don't have one). Create a `.env` file in the root of the project and put the following inside:

```text
TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Then to run the bot, simply use the command *(the token will automatically be loaded from the file into an environment variable)*:

```bash
pipenv run python index.py
```

### Using regular pip

If you don't want to use `pipenv`, you can manually install dependencies. Open `Pipfile` and look under the `[packages]` section and install all of the packages listed there using pip. For example, for `discord-py`, you would do:

```bash
python3 -m pip install discord-py
```

Before we run the bot, we need to set the Discord token (take a look [here](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) if you don't have one). This will depend on your operating system, so look at your specific one below. **These commands need to be run in every new terminal (psst, use pipenv if this is annoying).**

**Linux**

```bash
export TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

**Windows (PowerShell)**

```powershell
$env:TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
```

**Windows (cmd)**

```cmd
SET TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```
