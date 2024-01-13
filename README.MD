## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Running the App with AWS SAM CLI

To run this application, follow these steps:

1. **Navigate to the project directory in your terminal.**

2. **Build the SAM application:**

	```
	sam build
	```

3. **Deploy the SAM application:**

	```
	sam deploy --guided
	```

4. **Configure Telegram WebHook:**

	After deploying the application, configure the [Telegram Webhook](https://core.telegram.org/bots/api#setwebhook) using the API Gateway endpoint generated during the deployment.
	```
	Key                 tlgmBotRestApi
	Description         API Gateway endpoint URL for Telegram webHook
	Value               <Endpoint Value>
	```
5. **Configure Telegram WebHook:**
	Add Telegrab bot token into DynamoDB table 'tlgmSettings'
	```
	bot_id: 1
	token: token value
	```