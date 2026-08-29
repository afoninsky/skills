// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "CheckoutUI",
    platforms: [.iOS(.v17)],
    products: [.library(name: "CheckoutUI", targets: ["CheckoutUI"])],
    targets: [.target(name: "CheckoutUI", path: "Sources/Checkout")]
)

