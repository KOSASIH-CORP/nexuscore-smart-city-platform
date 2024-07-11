package main

import (
	"time"
)

type EnergyConsumption struct {
	ID             int       `json:"id"`
	Timestamp      time.Time `json:"timestamp"`
	EnergyConsumption float64 `json:"energy_consumption"`
}
