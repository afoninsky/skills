import SwiftUI

struct CheckoutSummaryView: View {
    let total: String

    var body: some View {
        VStack(alignment: .leading) {
            Text("Order total")
            Text(total)
        }
    }
}

