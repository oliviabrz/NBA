import { Component, OnInit } from '@angular/core';
import { Player } from '../player';
import { PLAYERS } from '../mock-players';
import { ApiDataService } from '../apiData/api.data.service';

@Component({
  selector: 'app-players',
  templateUrl: './players.component.html',
  styleUrls: ['./players.component.scss']
})
export class PlayersComponent implements OnInit {

  players: Player[] = new Array<Player>();
  selectedPlayer?: Player;
  displayedColumns  :  string[] = ['id', 'teamId', 'firstName', 'lastName', 'position', 'heightFeet', 'heightInches', 'weightPounds'];
  
  constructor(private apiDataService: ApiDataService) { 
    //console.info('In constructor')
  }

  ngOnInit(): void {
    //console.info('In ngOnInit')
    this.players = PLAYERS;
    // this.apiDataService.getPlayerList()
    // .subscribe((data) => {    
    //   this.players = data
    // });
  }

  onSelect(player: Player): void {
    this.selectedPlayer = player;
  }

}
