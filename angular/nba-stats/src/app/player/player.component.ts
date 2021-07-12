import { Component, OnInit } from '@angular/core';
import { Player } from '../player';
import { PLAYER } from '../mock-player';
import { Kvp } from '../kvp';
import { ApiDataService } from '../apiData/api.data.service';
import { MatTableDataSource } from '@angular/material/table';
import { AppStateService } from '../app-state';

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss']
})
export class PlayerComponent implements OnInit {
  player?: Player; 
  dsTable: MatTableDataSource<Kvp>;
  tableData: Kvp[] | undefined;

  //selectedTeam?: Team;
  displayedColumns  :  string[] = ['Key', 'Value'] 

  constructor(private appState: AppStateService) {
    this.dsTable = new MatTableDataSource<Kvp>();
   }
   
   ngOnInit(): void {     
    this.player = this.appState.selectedPlayer
      this.tableData = [
        {Key: 'FirstName', Value: this?.player?.FirstName},
        {Key: 'HeightFeet', Value: this?.player?.HeightFeet},
        {Key: 'HeightInches', Value: this?.player?.HeightInches},
        {Key: 'ID', Value: this?.player?.ID},
        {Key: 'LastName', Value: this?.player?.LastName},
        {Key: 'Position', Value: this?.player?.Position},
        {Key: 'TeamID', Value: this?.player?.TeamID},
        {Key: 'WeightPounds', Value: this?.player?.WeightPounds}
      ];
      this.dsTable.data = this.tableData;
    };
  }
