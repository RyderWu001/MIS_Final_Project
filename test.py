<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hi</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            font-family: "Microsoft JhengHei", sans-serif;
            overflow: hidden;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            animation: fadeIn 3s ease-in-out;
        }

        h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            letter-spacing: 5px;
        }

        p {
            font-size: 1.2rem;
            opacity: 0.8;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* 簡單的小裝飾 */
        .heart {
            color: #ff4d4d;
            font-size: 2rem;
            animation: beat .25s infinite alternate;
            display: inline-block;
        }

        @keyframes beat {
            to { transform: scale(1.2); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="heart">❤️</div>
        <h1>吳念琴 生日快樂~</h1>
        <p>這不是GPT</p>
    </div>
</body>
</html>