class Solution:
    def encode(self, strs: List[str]) -> str:
        result: str = ""
        for s in strs:
            result += f"{s}-"
        return result.strip()

    def decode(self, s: str) -> List[str]:
        result: List[str] = s.strip().split("-")
        result.pop()
        return result
