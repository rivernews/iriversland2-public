import { Component, OnInit, OnDestroy, Input, ElementRef, HostListener, ViewChild } from '@angular/core';

import { Subscription } from "rxjs";

import { ObjectDataService } from "../../services/object-data.service";
import { SnackBarServiceService } from "../../services/snack-bar-service.service";
import { ResponsiveService } from '../../services/responsive.service';

@Component({
    selector: 'app-highlighted-case-study',
    templateUrl: './highlighted-case-study.component.html',
    styleUrls: ['./highlighted-case-study.component.scss'],
})
export class HighlightedCaseStudyComponent implements OnInit, OnDestroy {
    private subscriptions = new Subscription();

    public isSubmitting: boolean = false;

    /** animations */
    @ViewChild('highlightedCaseStudyTextContainer') highlightedCaseStudyTextContainer: ElementRef;
    @ViewChild('highlightedCaseStudyContainer') highlightedCaseStudyContainer: ElementRef;

    @Input()
    public highlightedCaseStudy: any;
    @Input()
    public isLogin: boolean = true;    
    @Input()
    public highlightedCaseStudyIndex: number;

    constructor(
        private objectDataService: ObjectDataService,
        private barService: SnackBarServiceService,
        public responsiveService: ResponsiveService,

        public el: ElementRef
    ) { }

    ngOnInit() {
    }

    ngOnDestroy() {
        this.subscriptions.unsubscribe();
    }

    onSubmitClick(highlightedCaseStudyData?) {
        this.isSubmitting = true;
        if (highlightedCaseStudyData) {
            this.updateHighlightedCaseStudy(highlightedCaseStudyData);
        }
    }

    updateHighlightedCaseStudy(highlightedCaseStudyData) {

        this.subscriptions.add(this.objectDataService.update('highlighted-case-studies', highlightedCaseStudyData).subscribe(
            success => {
                this.barService.popUpMessage("✅ Submitted highlight study successfully");
            },
            error => {
                this.barService.popUpMessage("Failed to submit highlight study");
            },
            () => {
                this.isSubmitting = false;
            }
        ));
    }

    /**
     * 
     * Scrolling Animation
     * 
     */

    @HostListener('window:scroll', ['$event'])
    private scrollController(e) {
        const component = this.el.nativeElement;
        const container = this.highlightedCaseStudyContainer.nativeElement;
        const textContainer = this.highlightedCaseStudyTextContainer.nativeElement;

        let highlightedTextTriggerPosition = (this.responsiveService.isMobilePhone) ? 0.45 : 0.85;
        if (this.isElementInViewport(component, highlightedTextTriggerPosition)) {
            container.classList.add('shaded');

            textContainer.classList.add('show-state');
            textContainer.classList.remove('hide-state');
        } else {
            container.classList.remove('shaded');
            
            textContainer.classList.remove('show-state');
            textContainer.classList.add('hide-state');
        }
    }

    private isElementInViewport(el, portion?) {
        let portionTrigger = 1;    
        if (portion) {
            portionTrigger = portion;            
        }

        let rect = el.getBoundingClientRect();

        let elementHeight = rect.height;
        let viewportHeight = (window.innerHeight || document.documentElement.clientHeight);
        let emergedHeight = viewportHeight - rect.top;

        // console.log(`emergedH: ${emergedHeight}, portion: ${portionTrigger}, elementH: ${elementHeight}`);

        return (
            emergedHeight >= 0 &&
            emergedHeight >= portionTrigger * elementHeight
            // rect.top >= 0 &&
            // rect.left >= 0 &&
            // rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) /*or $(window).height() */
            // rect.right <= (window.innerWidth || document.documentElement.clientWidth) /*or $(window).width() */
        );
    }
}
