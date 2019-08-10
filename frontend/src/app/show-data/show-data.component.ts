import { Component, OnInit, OnDestroy } from '@angular/core';
// import { Http } from '@angular/http';
import { ApiService } from '../api.service';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-show-data',
  templateUrl: './show-data.component.html',
  styleUrls: ['./show-data.component.css'],
  providers: [ApiService]
})
export class ShowDataComponent implements OnInit, OnDestroy {
  private listSub: Subscription[] = [];
  products : any = [];
  constructor(
    private api: ApiService,
    private route: ActivatedRoute
  ) {
    this.getProducts();
  }

  getProducts = () => {
    this.listSub.push(
      this.api.getAllProduct().subscribe(
        data => {
          this.products = data;
        },
        error => {
          console.log(error);
        }
      )
    );
  }

  ngOnInit() {
    let token = localStorage.getItem('token');
    console.log(token);
    
    // if(token) {
    //   this.api.getCurrentUser().subscribe(
    //     data => {
    //       console.log(data);
    //     },
    //     error => {
    //       console.log(error);
    //     }
    //   )
    // }
  }

  ngOnDestroy(){
    this.listSub.forEach(sub => sub.unsubscribe());
  }

}
