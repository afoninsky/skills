import SwiftUI
import UIKit

final class CheckoutCoordinator {
    func makeSummary() -> UIViewController {
        UIHostingController(rootView: CheckoutSummaryView(total: "$48.00"))
    }
}

