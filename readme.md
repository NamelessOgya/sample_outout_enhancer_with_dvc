
# 基本思想  
実行時のid(mikoto_run_id) を生成し  
`git commit`の時にtagとして登録することで、生成物とコードの紐づけを行う。  
mlflowによりcommit idと実行結果の紐づけを行う。  
  
  
## run  
`feedback`を考慮して、プロンプトを次の世代に進化させる。  
```
poetry run dvc repro evolve --generation 2 
```  
  

`feeedback`を作成する。
```
poetry run dvc repro feedback --generation 2 
```  
  
## 出力物  
### ./data/gen{genearation}_{mokoto_run_id}/prompts.txt  
プロンプトのエンハンスを行う場合、  
この部分にプロンプトが蓄積される。
  
### ./data/gen{genearation}_{mokoto_run_id}/evolve_result.csv  
生成を行う場合、
- {generate_target.csv}に含まれるカラム  
  - evolve時の出力に文字列insertされる。
  
### ./data/gen{genearation}_{mokoto_run_id}/feedback_result.csv  
`evolve_result.csv`のアウトプット項目に`score`が追加された形。  
`make_feedback`を用いて作成してもいいし、自分で作成してもいい。  
  


