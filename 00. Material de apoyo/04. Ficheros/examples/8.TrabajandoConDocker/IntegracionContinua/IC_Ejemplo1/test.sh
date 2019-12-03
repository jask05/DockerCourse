#!/bin/bash
echo "Empezando test"
sleep 3
echo "Ejecutando test"
if curl 192.168.1.102:5005 | grep -q 'Detalles de visitas'; then
  echo "Tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi
