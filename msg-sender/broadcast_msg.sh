curl -v -X POST https://api.line.me/v2/bot/message/broadcast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer [your-key]' \
-d '{
    "messages":[
        {
            "type":"text",
            "text":"嗨，您好，感謝您使用 NTU-GYM-LINE-BOT，為了提供給您更好的使用體驗，我們將於今日(3/26) 晚上 9 時暫停服務，並於隔日凌晨恢復運作。感謝您的配合：）"
        }
    ]
}'