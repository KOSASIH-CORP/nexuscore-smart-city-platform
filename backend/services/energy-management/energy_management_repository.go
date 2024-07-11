package main

import (
	"database/sql"
	"log"
)

type EnergyManagementRepository struct {
	db *sql.DB
}

func NewEnergyManagementRepository(db *sql.DB) *EnergyManagementRepository {
	return &EnergyManagementRepository{db: db}
}

func (r *EnergyManagementRepository) GetEnergyConsumption() ([]EnergyConsumption, error) {
	rows, err := r.db.Query("SELECT * FROM energy_consumption")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var energyConsumptions []EnergyConsumption
	for rows.Next() {
		var ec EnergyConsumption
		err := rows.Scan(&ec.ID, &ec.Timestamp, &ec.EnergyConsumption)
		if err != nil {
			return nil, err
		}
		energyConsumptions = append(energyConsumptions, ec)
	}
	return energyConsumptions, nil
}

func (r *EnergyManagementRepository) CreateEnergyConsumption(ec EnergyConsumption) error {
	_, err := r.db.Exec("INSERT INTO energy_consumption (timestamp, energy_consumption) VALUES (?, ?)", ec.Timestamp, ec.EnergyConsumption)
	return err
}
