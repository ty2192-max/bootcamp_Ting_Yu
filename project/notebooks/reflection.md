### Risks if deployed: 
The model faces data drift risks from changing market conditions that could break the linear relationship assumption. Missing data patterns may shift, reducing imputation effectiveness. Outlier detection could fail during high volatility periods, either missing real anomalies or filtering legitimate opportunities. System latency could increase during market open hours, causing delayed predictions.

### Monitoring metrics: 
Data layer: freshness (<5 minutes delay), null rate (<2% increase), schema changes (daily validation). Model layer: rolling 7-day MAE (<1.0 threshold), weekly PSI (<0.1 on key features). System layer: p95 latency (<200ms), error rate (<1%). Business layer: prediction accuracy (>70% daily), strategy performance vs benchmark.

### Ownership & handoffs: 
Data engineers own data pipeline monitoring with 24/7 alerting. ML engineers handle model performance with weekly reviews. System reliability team monitors API endpoints during trading hours. Business analysts verify daily performance reports. Handoffs occur through dedicated Slack channels and weekly sync meetings. Critical alerts (p95 latency >250ms or MAE >1.5) trigger immediate on-call notifications to relevant teams. Retraining occurs automatically when PSI >0.15 or weekly MAE increases by 20%.