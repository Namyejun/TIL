## 머신러닝 모델의 평가지표

### 회귀(Regression) 모델의 평가 지표

- RMSE(Root Mean Square Error)
    
    $\sqrt {\frac {1} {n} \sum_{i = 1}^n (y_i - \hat y_i)^2 }$
    
    $y_i$ : i번째 자료의 label
    
    $\hat y_i$ : i번쨰 자료의 모형 예측값
    
- R-square, $R^2$ (결정계수) : 회귀분석에서 많이 사용하는 지표
    
    $1 - \dfrac {\sum_{i = 1}^n (y_i - \hat y_i)^2} {\sum_{i = 1}^n (y_i - \bar y)^2} = 1 -\dfrac {SSE} {SST} = \dfrac {SSR} {SST}$
    
    $y_i$ : i번째 자료의 label
    
    $\hat y_i$ : i번쨰 자료의 모형 예측값
    
    $\bar y$ : label 들의 평균
    
    0이면 모형이 안좋고 1이면 모델이 완벽한 피팅을 한 상태
    
- MAE (Mean Absolute Error)
    
    $\dfrac 1 n \displaystyle\sum_{i=1}^{n}  \bigg| \dfrac {y_i - \hat y_i} {y_i} \bigg|$
    
    1. 오차의 부포만 제거해서 이를 평균한 값
    2. MAE가 10이면 오차가 평균적으로 10정도 발생한다고 이해.

- MAPE(Mean Absolute Percentage Error)
    
    $100 \times \bigg(\dfrac 1 n \displaystyle\sum_{i=1}^n \bigg|\dfrac {y_i - \hat y_i} {y_i} \bigg| \bigg)$
    
    1. 실제 값 대비 오차가 차지하는 비중이 평균적으로 얼마인지 확인
    

### 분류(Classification) 모델의 평가 지표

- 정오분류표(Confusion Matrix)
    
    ![Untitled](img/Untitled%201.png)
    
    맞혔는지 틀렸는지 여부에 대해 앞이 결정, 모형에 의한 예측값에 의해 뒤가 결정
    
- 정확도, 정분류율(Accuracy)
    - 전체관찰치중 정분류된 관찰치의 비중
        
        $\dfrac {TN + TP} {TN + FP + FN + TP}$
        

- 정밀도(Precision)
    - Positive로 예측한 것 중에서 실제 범주도 Positive인 데이터의 비율.
        
        $\dfrac {TP} {FP + TP}$
        
- 재현율(Recall)
    - 실제 범주가 Positive인 것 중에서 Positive로 예측된 데이터의 비율.
        
        $\dfrac {TP} {FN + TP}$
        
    
- ROC(Receiver Operation Characteristic) 도표
    - 분류의 결정 임계값(threshold)에 따라 달라지는 TPR(민감도, Sensitivity)과
        
        FPR(1-특이도, 1 - Specificity)의 조합을 도표로 나타냄.
        
        1. TPR : True Positive Rate (= Sensitivity(민감도))
        1인 케이스에 대해 1로 잘 예측한 비율 = 재현율
        2. FPR : False Positive Rate (= 1 - Specificity(특이도))
        0인 케이스에 대해 1로 잘못 예측한 비율
            
            $\dfrac {FP} {TN + FP}$
            
        3. 임계값이 1이면 FPR = 0, TPR = 0
        4. 임계값을 1에서 0으로 낮춰감에 따라 FPR과 TPR은 동시에 증가함.
        5. FPR이 증가하는 정도보다 TPR이 빠르게 증가하면 이상적
        → 왼쪽 위 꼭지점에 가까울수록 좋음
        
        ![Untitled](img/Untitled%202.png)
        

- AUC(Area Under the Curve)
    - ROC 곡선 아래의 면적
    - 가운데 대각선의 직선은 랜덤한 수준의 이진 분류에 대응되며,
    이 경우 AUC는 0.5임.
    - 1에 가까울수록 좋은 수치. FPR이 작을 때 얼마나 큰 TPR을 얻는지에 따라 결정됨.
    
