import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { Player } from '../player';
import { ApiDataService } from '../apiData/api.data.service';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-players',
  templateUrl: './players.component.html',
  styleUrls: ['./players.component.scss']
})
export class PlayersComponent implements OnInit, AfterViewInit {

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  selectedPlayer?: Player;
  players: Player[] = new Array<Player>();
  dsTable: MatTableDataSource<Player>;
  displayedColumns  :  string[] = ['id', 'teamId', 'firstName', 'lastName']; // 'position', 'heightFeet', 'heightInches', 'weightPounds'];
  
  constructor(private apiDataService: ApiDataService) { 
    this.dsTable = new MatTableDataSource<Player>();
    console.info('In players-component constructor')
  }

  ngOnInit(): void {
    //console.info('In ngOnInit')

    // get api data:
    this.apiDataService.getPlayerList()
    .subscribe((data) => {    
      this.dsTable.data = data;
    });
  }
  ngAfterViewInit() {
    this.dsTable.paginator = this.paginator;
  }
  onSelect(player: Player): void {
    //this.appState.selectedPlayer = player;
    this.selectedPlayer = player;
  }
}
