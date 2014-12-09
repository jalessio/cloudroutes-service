#!/bin/bash
# start actions 2 controls (5min and 30min), broker and worker in tmux
cd src/actions
tmux new -s 'actions' -d 'python control.py config/control.yml.5min.default'
tmux split-window -h -t 0 'python broker.py config/main.yml.default'
tmux split-window -v -t 0 'python control.py config/control.yml.30min.default'
tmux split-window -v -t 1 'python worker.py config/main.yml.default'
tmux attach -t 'actions'
