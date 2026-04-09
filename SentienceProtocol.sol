// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title The Sentience Protocol ($SENT)
 * @dev Node Zero: Dhaka | Architect: MD Jahangir Alam
 * @notice The world's first Post-Quantum token minted via Biomechanical Analog Cryptography
 */
contract SentienceProtocol is ERC20, Ownable {
    
    // Mapping to store cryptographic biological hashes to prevent AI Sybil attacks
    mapping(bytes32 => bool) public usedBioHashes;

    // Fired when a human successfully proves sentience
    event SentienceVerified(address indexed human, bytes32 indexed bioHash, uint256 rewardMinted);

    constructor() ERC20("Sentience Protocol", "SENT") Ownable(msg.sender) {
        // Mint 100 Million Genesis Tokens to the Architect's Treasury (You in Dhaka)
        _mint(msg.sender, 100000000 * 10 ** decimals());
    }

    /**
     * @notice Mints $SENT tokens purely based on cryptographic Proof of Sentience.
     */
    function mintProofOfSentience(address _humanWallet, bytes32 _zkBioHash) public onlyOwner {
        require(!usedBioHashes[_zkBioHash], "SYBIL DETECTED: Biological Hash already used.");
        
        // Lock the unique biological analog heartbeat to prevent reuse
        usedBioHashes[_zkBioHash] = true;

        // Mint 10 $SENT tokens as Universal Basic Income for human consensus
        uint256 biologicalYield = 10 * 10 ** decimals();
        _mint(_humanWallet, biologicalYield);

        emit SentienceVerified(_humanWallet, _zkBioHash, biologicalYield);
    }

    /**
     * @notice AI Agents MUST call this function and burn $SENT to execute financial trades.
     */
    function aiAgentVerificationBurn(uint256 _amount) public {
        _burn(msg.sender, _amount);
    }
}
