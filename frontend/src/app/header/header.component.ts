import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit, OnDestroy {
  private listSub : Subscription[] = [];

  authenticated : string = "";
  current: any = {};
  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private api: ApiService
  ) { }

  ngOnInit() {
    this.authenticated = localStorage.getItem('token') || "";
    if(this.authenticated != "") {
      this.listSub.push(
        this.api.getCurrentUser().subscribe(
          data => {
            console.log(data);
            this.current = data;
          },
          error => {
            console.log(error);
          }
        )
      );
    }
  }

  onLogout() {
    localStorage.removeItem('token');
    this.authenticated = "";
    this.router.navigate(['/']);
  }

  ngOnDestroy(): void {
    this.listSub.forEach(sub => sub.unsubscribe());
  }
}
