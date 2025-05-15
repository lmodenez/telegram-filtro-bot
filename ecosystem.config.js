module.exports = {
  apps: [
    {
      name: "telegram-bot",
      script: "docker",
      args: "run telegram-bot",
      interpreter: "none"
    }
  ]
}