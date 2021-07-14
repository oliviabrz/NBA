import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'; // <-- NgModel lives here
import { MatTableModule } from "@angular/material/table";
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSelectModule } from '@angular/material/select';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PlayersComponent } from './players/players.component';
import { TeamComponent } from './team/team.component';
import { KeyValuePipeComponent } from './keyvalue-pipe/keyvalue-pipe.component';
import { PlayerComponent } from './player/player.component';
import { TeamListComponent } from './team-list/team-list.component';
import { GameListComponent } from './game-list/game-list.component';

@NgModule({
  declarations: [
    AppComponent,
    PlayersComponent,
    TeamComponent,
    KeyValuePipeComponent,
    PlayerComponent,
    TeamListComponent,
    GameListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    MatTableModule,
    MatPaginatorModule,
    MatSelectModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
