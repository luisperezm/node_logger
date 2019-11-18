# Node logger

## Dependencies

```bash
pip install azure_eventhub
```

## How to compile it
```bash
cd ~/cokoon_ws/src
git clone https://gitlab.com/nttdisruption/cokoon/ros2/core/node_logger.git
```

Now you can compile it:

```bash
cd ~/cokoon_ws
source /opt/ros/dashing/setup.bash
colcon build --merge-install
```

## How to launch it
- Dashing
```bash
source ~/cokoon_ws/install/setup.bash
ros2 run node_logger node_logger.py --ros-args --remap __ns:=/eventhub_credentials -p $(ros2 pkg prefix node_logger)/share/node_logger/config/eventhub_credentials.yaml
```