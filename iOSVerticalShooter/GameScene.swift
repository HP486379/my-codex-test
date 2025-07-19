import SpriteKit
import GameplayKit

class GameScene: SKScene {
    let player = SKSpriteNode(color: .green, size: CGSize(width: 40, height: 40))

    override func didMove(to view: SKView) {
        backgroundColor = .black
        player.position = CGPoint(x: size.width / 2, y: player.size.height * 2)
        addChild(player)
        spawnEnemy()
    }

    func spawnEnemy() {
        let enemy = SKSpriteNode(color: .red, size: CGSize(width: 40, height: 40))
        enemy.position = CGPoint(x: size.width / 2, y: size.height - enemy.size.height)
        addChild(enemy)
        let moveDown = SKAction.moveTo(y: -enemy.size.height, duration: 3)
        let remove = SKAction.removeFromParent()
        enemy.run(SKAction.sequence([moveDown, remove]))
    }

    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let touch = touches.first else { return }
        let location = touch.location(in: self)
        player.position.x = location.x
    }
}
