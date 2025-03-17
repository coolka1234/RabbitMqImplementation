python3 -m typeOnePublisher.App.publish &
python3 -m typeOnePublisher.App.publish &
python3 -m typeOnePublisher.App.publish &
python3 -m typeTwoPublisher.App.publish &
python3 -m typeThreePublisher.App.publish &
python3 -m typeFourPublisher.App.publish &
python3 -m typeOneConsumer.App.consume &
python3 -m typeOneConsumer.App.consume &
python3 -m typeTwoConsumer.App.consume &
python3 -m typeThreeConsumer.App.consume & 
python3 -m typeFourConsumer.App.consume &

read

killall python3