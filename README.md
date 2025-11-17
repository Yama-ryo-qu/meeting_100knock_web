**【Web開発100本ノック】**



以下テーマ2の解答


**課題26**

<img width="950" height="872" alt="スクリーンショット (161)" src="https://github.com/user-attachments/assets/ce9c4569-4cd6-40b2-8083-14106f7f7112" />

講義：ウェブサービスデザインの内容を参考にしています。


        .geiko1 {
            background: blue;
            margin: 5px;
        }

flexboxの指定なし➡縦に並んで表示

        .geiko2 {
            background: blue;
            margin: 5px;
            display: flex;
        }

flexboxを指定する➡横並びで配置される。ただし、ブラウザの画面幅を小さくしても要素は折り返されない

        .geiko3 {
            background: blue;
            margin: 5px;
            display: flex;
            flex-wrap: wrap;
        }

flex-warp: wrapを指定する➡要素が入り切らない場合に折り返される

        .geiko4 {
            background: blue;
            margin: 5px;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

justify-content: centerを指定する➡要素が中揃えされる

        .geiko5 {
            background: blue;
            margin: 5px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }

justify-content: space-aroundを指定する➡要素が均等割りされる
