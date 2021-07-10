import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { Player } from '../player';
import { PLAYERS } from '../mock-players';
import { ApiDataService } from '../apiData/api.data.service';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { AppComponent } from '../app.component';


@Component({
  selector: 'app-players',
  templateUrl: './players.component.html',
  styleUrls: ['./players.component.scss']
})
export class PlayersComponent implements OnInit, AfterViewInit {

  @ViewChild(MatPaginator) paginator!: MatPaginator;

  players: Player[] = new Array<Player>();
  dsTable: MatTableDataSource<Player>;
  selectedPlayer?: Player;
  displayedColumns  :  string[] = ['id', 'teamId', 'firstName', 'lastName', 'position', 'heightFeet', 'heightInches', 'weightPounds'];
  
  constructor(private apiDataService: ApiDataService,
    public appComponent: AppComponent) { 
    this.dsTable = new MatTableDataSource<Player>();
    //console.info('In constructor')
  }

  ngOnInit(): void {
    //console.info('In ngOnInit')

    // this is api data:
    this.apiDataService.getPlayerList()
    .subscribe((data) => {    
      this.dsTable.data = data;
    });
  }
  ngAfterViewInit() {
    this.dsTable.paginator = this.paginator;
  }
  onSelect(player: Player): void {
    this.selectedPlayer = player;
  }
  showAlert(player: Player) {
    //alert(player.FirstName)
    this.appComponent.playerDetailVisible = !this.appComponent.playerDetailVisible;
  }
}
