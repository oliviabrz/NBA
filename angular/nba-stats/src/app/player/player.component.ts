import { Component, OnInit, Input, OnChanges, SimpleChanges } from '@angular/core';
import { Player } from '../player';
import { Kvp } from '../kvp';
import { MatTableDataSource } from '@angular/material/table';
@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss']
})
export class PlayerComponent implements OnInit, OnChanges {
  @Input() selectedPlayer?: Player;
  dsTable: MatTableDataSource<Kvp>;
  tableData: Kvp[] | undefined;
  displayedColumns  :  string[] = ['Key', 'Value'] 

  constructor() {
    this.dsTable = new MatTableDataSource<Kvp>();
   }
   
   ngOnInit(): void { };

    ngOnChanges(changes: SimpleChanges) {
      // only run when property "selectedPlayer" changed
      let player = changes['selectedPlayer'].currentValue
      if (player != undefined) {
        console.info("in player-component ngOnChanges: selectedPlayer not null");
        this.tableData = [
          {Key: 'First Name', Value: player.FirstName},
          {Key: 'Last Name', Value: player.LastName},
          {Key: 'Position', Value: player.Position},
          {Key: 'Weight (lbs)', Value: player.WeightPounds},
          {Key: 'Height (ft)', Value: player.HeightFeet},
          {Key: 'Height (in)', Value: player.HeightInches},
  
        ];
        this.dsTable.data = this.tableData;
      }
      else {
        console.info("in player-component ngOnChanges: selectedPlayer null");
      }   
  }
}
