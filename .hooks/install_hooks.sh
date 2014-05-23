#!/bin/bash
rsync -av --progress * ../.git/hooks --exclude install_hooks.sh
