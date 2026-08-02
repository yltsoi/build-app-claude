import Anthropic from "@anthropic-ai/sdk";
import dotenv from "dotenv";
import express from "express";

dotenv.config();
const app = express();
app.use(express.json());

const client = new Anthropic({maxRetries: 3});

async function askCalude(prompt: string)  : Promise<string> {
    const messages = await client.messages.create({
        model: "claude-haiku-4-5",
        max_tokens: 256,
        messages: [{
            role: "user",
            content: prompt
        }],
    });
    return (messages.content[0] as any).text;


    app.post("/summarize", async (req, res) => {
        const summary = await askCalude( `Summarize this\n: ${req.body.text}` );
        res.json({ summary });
    }); 

    app.listen(3000, () => {
        console.log("Server is running on port 3000");
    });

    