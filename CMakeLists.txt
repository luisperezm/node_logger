cmake_minimum_required(VERSION 3.5)
project(node_logger)

if(NOT CMAKE_CXX_STANDARD)
 set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
 add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

install(PROGRAMS
  scripts/node_logger.py
  scripts/message_sender.py
  scripts/listeners/rosout_listener.py
  scripts/listeners/string_listener.py
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
    config
 DESTINATION share/${PROJECT_NAME}
)

ament_package()

