**【Web開発100本ノック】**



以下テーマ3の解答


**課題31**

**1. 変数**

        let userName = "山田 太郎";
        const userAge = 30;
        var isStudent = false;
   
        console.log("--- 変数 ---");
        console.log("名前:", userName);
        console.log("年齢:", userAge);
        console.log("学生:", isStudent);

結果

<img width="1548" height="128" alt="スクリーンショット (162)" src="https://github.com/user-attachments/assets/79f443bd-de34-45ce-9cbe-ad02a816fcd1" />

・let➡再代入〇、再宣言✕

・const➡再代入✕、再宣言✕　（つまり定数）

・var➡再代入〇、再宣言〇　（※古い変数宣言方法、非推奨）

以下例（https://techplay.jp/column/1619より）

        // 再宣言
        var hoge1 = 1;
        var hoge1 = 2;
        console.log(hoge1);  // 2
 
        let hoge2 = 1;
        let hoge2 = 2; // ここでエラーが発生
 
        const hoge3 = 1;
        const hoge3 = 2; // ここでエラーが発生

        // 再代入
        var hoge1 = 1;
        hoge1 = 2;
        console.log(hoge1);  // 2

        let hoge2 = 1;
        hoge2 = 2;
        console.log(hoge2);  // 2
 
        const hoge3 = 1;
        hoge3 = 2; // ここでエラーが発生

**2. 配列**

        const colors = ["Red", "Green", "Blue"];

        console.log("--- 配列 ---");
        console.log("色リスト:", colors);
        console.log("3番目の色 (インデックス2):", colors[2]);

結果

<img width="963" height="100" alt="スクリーンショット (162)" src="https://github.com/user-attachments/assets/bb3e3870-c5e8-4144-ae15-a80f830921e5" />

・配列内の要素の同時出力

・配列のインデックス使って、特定の要素を出力

**3. オブジェクト**
   
        const userProfile = {
          id: "A001",
          name: "佐藤 花子",
          occupation: "エンジニア",
          hobbies: ["読書", "サイクリング"]
        };

        console.log("--- オブジェクト ---");
        console.log("ユーザープロフィール:", userProfile);
        console.log("ユーザー名:", userProfile.name);
        console.log("職業:", userProfile["occupation"]);


 結果

<img width="1259" height="136" alt="スクリーンショット (162)" src="https://github.com/user-attachments/assets/da78ba9e-9622-4c13-933e-737983135fb0" />

・オブジェクトuserProfileの全プロパティをコンソールに出力

・ドット記法（.）を使って、キーnameの値（"佐藤 花子"）を出力

・ブラケット記法（[]）を使って、キーoccupationの値（"エンジニア"）を出力
 
