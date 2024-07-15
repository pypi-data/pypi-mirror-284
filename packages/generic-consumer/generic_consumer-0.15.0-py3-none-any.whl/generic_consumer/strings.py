from simple_chalk import chalk

WARN_CONSUMER_DISABLED: str = chalk.yellow(
    f"'{chalk.white('{queue_name}')}' was disabled during runtime!",
)
ERROR_NO_ACTIVE_CONSUMER: str = "No non-passive consumers for '{queue_name}'!"
ERROR_PAYLOAD: str = chalk.yellow("Payload processing error!")
INFO_PAYLOAD: str = chalk.green(
    f"Got {chalk.white('{count}')} payload(s) from '{chalk.white('{queue_name}')}'.",
)
